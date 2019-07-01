from settings import CORE_PATH
from utils.configuration import config_core
from utils.dockerUtiles import make_docker_image, build_docker_images, build_network, compose_core, compose_http
from utils.utils import startup


def main():
    # startup()
    config_core()
    # build_docker_images()
    # build_network()
    compose_core()
    compose_http()

if __name__ == '__main__':
    main()
