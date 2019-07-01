import os
import subprocess

import docker
from settings import *

docker_client = docker.from_env()


def make_docker_image(project_path):
    print(">>> Building core docker image of {}".format(project_path))
    subprocess.call(['make', '-C', project_path, 'docker_build'])


def build_docker_images():
    make_docker_image(CORE_PATH)
    make_docker_image(HTTP_PATH)


def build_network():
    print(">>> Building {} docker network".format(NETWORK_NAME))
    if len(docker_client.networks.list([NETWORK_NAME])) > 0:
        print(">>> {} is already exist".format(NETWORK_NAME))
        # return
    ipam_pool = docker.types.IPAMPool(
        subnet=NETWORK_SUBNET,
        gateway=NETWORK_GATEWAY
    )

    ipam_config = docker.types.IPAMConfig(
        pool_configs=[ipam_pool]
    )
    try:
        docker_client.networks.create(name=NETWORK_NAME, driver="bridge", ipam=ipam_config)
    except docker.errors.APIError as err:
        print("Error while building {}:\n\t{}".format(NETWORK_NAME, err))


def compose_header(f):
    f.write(
'version: "2.1"\n\
services:\n'
    )


def compose_core():
    print(">>> Generate core compose file")
    os.makedirs(os.path.join(ENV_DIR, 'composed'), exist_ok=True)
    f = open(os.path.join(ENV_DIR, 'composed', 'core_compose.yml'), "w+")
    compose_header(f)
    for i in range(CLUSTER_SIZE):
        compose_core_server(i, f)
    compose_footer(f)
    f.close()


def compose_core_server(id, f):

    from utils.utils import create_ip
    f.write(
'\t                                                                                                                                                 {}{}:\n\
    image: {}\n\
    container_name: {}_{}\n\
    environment:\n\
    - ID={}\n\
    - Type=r\n\
    volumes:\n\
    - {}:/tmp/JToy\n\
    - {}:/JToy/bin/src/main/resources\n\
    networks:\n\
        {}:\n\
            ipv4_address: {}\n'.format(CORE_SERVER, id, CORE_IMAGE,CORE_SERVER,
                                       id, id, os.path.join(OUT_DIR, CORE_SERVER),
                                         CORE_ENV_DIR, NETWORK_NAME, create_ip(NETWORK_SUBNET, id + 3))
    )


def compose_footer(f):
    f.write(
'networks:\n\
    {}:\n\
         external: true\n'.format(NETWORK_NAME)
    )


def compose_http_server(id, f):
    from utils.utils import create_ip
    f.write(
'\t{}{}:\n\
    image: {}\n\
    container_name: {}_{}\n\
    environment:\n\
    - ID={}\n\
    - IP={}\n\
    - PORT={}\n\
    - CORE_IP={}\n\
    - CORE_PORT={}\n\
    volumes:\n\
    - {}:/tmp/Spinner\n\
    ports:\n\
    - {}:{}\n\
    networks:\n\
        {}:\n\
            ipv4_address: {}\n'.format(HTTP_SERVER, id, HTTP_IMAGE, HTTP_SERVER, id, id,
                                       create_ip(NETWORK_SUBNET, id + CLUSTER_SIZE + 3),
                                       HTTP_PORT, create_ip(NETWORK_SUBNET, id + 3), CORE_DOCKER_RPC_PORT
                                        , os.path.join(OUT_DIR, HTTP_SERVER), HOST_BOUNDED_PORT + id, HTTP_PORT
                                    , NETWORK_NAME, create_ip(NETWORK_SUBNET, id + CLUSTER_SIZE + 3))
    )


def compose_http():
    print(">>> Generate http compose file")
    os.makedirs(os.path.join(ENV_DIR, 'composed'), exist_ok=True)
    f = open(os.path.join(ENV_DIR, 'composed', 'http_compose.yml'), "w+")
    compose_header(f)
    for i in range(CLUSTER_SIZE):
        compose_http_server(i, f)
    compose_footer(f)
    f.close()

