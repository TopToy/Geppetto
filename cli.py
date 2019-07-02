import shutil
import subprocess
import time
from sys import stdout

import click

from settings import *
from utils.configuration import config_tools
from utils.dockerUtiles import build_docker_images, build_network, compose_tools, docker_client
from utils.utils import install_tools


def setup_environment():
    install_tools()
    config_tools()
    build_docker_images()
    build_network()
    return compose_tools()


def run_cluster(compose_files):
    ret = []
    print(">>> Running {} cluster".format(CORE_SERVER))
    ret += [subprocess.call(['docker-compose', '-f', compose_files[0], 'up', '-d'], stdout=stdout)]
    print(">>> Waiting for cluster containers creation")
    while not ['{}_{}'.format(CORE_SERVER, id) for id in range(CLUSTER_SIZE)] <= \
        [d.name for d in docker_client.containers.list(filters={'ancestor': CORE_IMAGE})]:
        time.sleep(1)
    print(">>> Waiting until all containers are in 'running' state")
    while len(set([d.status for d in docker_client.containers.list(filters={'ancestor': CORE_IMAGE})])) > 1 \
        and [d.status for d in docker_client.containers.list(filters={'ancestor': CORE_IMAGE})][0] != 'running':
        time.sleep(1)
    print(">>> Running {} cluster, each frontend is connected to one {} server".format(HTTP_SERVER, CORE_SERVER))
    ret += [subprocess.call(['docker-compose', '-f',
                             os.path.join(ENV_DIR, 'composed', 'http_compose.yml'), 'up', '-d'], stdout=stdout)]
    return ret


def cli_stop():
    print(">>> Stopping all {} containers".format(CORE_SERVER))
    for c in docker_client.containers.list(filters={'ancestor': CORE_IMAGE}):
        c.stop()
    print(">>> Stopping all {} containers".format(HTTP_SERVER))
    for c in docker_client.containers.list(filters={'ancestor': HTTP_IMAGE}):
        c.stop()


def cli_clean():
    print(">>> removing all {} containers".format(CORE_SERVER))
    for c in docker_client.containers.list(filters={'ancestor': CORE_IMAGE}):
        c.remove()
    print(">>> removing all {} containers".format(HTTP_SERVER))
    for c in docker_client.containers.list(filters={'ancestor': HTTP_IMAGE}):
        c.remove()
    print(">>> removing {} network".format(NETWORK_NAME))
    for net in docker_client.networks.list(names=[NETWORK_NAME]):
        net.remove()
    shutil.rmtree(WORKING_DIR, ignore_errors=True)


@click.group()
def main():
    setup_env()
    pass


@main.command()
def install():
    """
    'Download and install {} and {} last versions'.format(CORE_SERVER, HTTP_SERVER)
    """
    install_tools()


@main.command()
def config():
    """
    Creates the desired configuration file w.r.t the settings.py file
    """
    config_tools()


@main.command()
def build():
    """
    Build the necessary docker objects
    """
    build_docker_images()
    build_network()
    compose_tools()


@main.command()
def setup():
    """
    Install and build
    """
    setup_environment()


@main.command()
def run():
    """
    Run a docker cluster of size CLUSTER_SIZE.
    The cluster composed of N core servers and corresponding N frontend servers, each has its own unique IP.
    Negotiation with the cluster is done by RESTful API as indicated in https://github.com/TopToy/Spinner.git.
    Note that the i_th frontend server is bounded to ports 8000 + i (you may configure this in settings.py)
    """
    run_cluster([os.path.join(ENV_DIR, 'composed', 'core_compose.yml'),
                 os.path.join(ENV_DIR, 'composed', 'http_compose.yml')])


@main.command()
def stop():
    """
    Stop all the cluster running containers
    """
    cli_stop()


@main.command()
def clean():
    """
    Remove all the cluster docker containers and delete the working dir.
    Note that this command does not remove the generated docker images.
    To remove them type:
    docker images rm toy:0.1
    docker images rm spinner:0.1
    """
    cli_clean()

# if __name__ == '__main__':
#     main()

