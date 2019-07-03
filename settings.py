import os

# Global settings #
CORE_SERVER = 'TopToy'
CORE_GIT_URL = 'https://github.com/TopToy/TopToy.git'
HTTP_SERVER = 'Spinner'
HTTP_GIT_URL = 'https://github.com/TopToy/Spinner.git'
WORKING_DIR = '/tmp/Geppetto_wd'
BASE_URL = 'http://[ip]:[port]/toptoy/'

# Environment settings #
ENV_DIR = os.path.join(WORKING_DIR, 'env')
CORE_ENV_DIR = os.path.join(ENV_DIR, CORE_SERVER)
HTTP_ENV_DIR = os.path.join(ENV_DIR, HTTP_SERVER)
CORE_PATH = os.path.join(WORKING_DIR, CORE_SERVER)
HTTP_PATH = os.path.join(WORKING_DIR, HTTP_SERVER)
OUT_DIR = os.path.join(WORKING_DIR, 'out')

# Core deployment settings #
CLUSTER_SIZE = 1
POSSIBLE_FAILURES = 0
WORKERS = 1
BLOCK_SIZE = 1000
INIT_TMO = 100

## Ports
WRB_PORT = 30000
OBBC_PORT = 30010
COMM_PORT = 30020
AB_PORT = 12000

# Docker settings
NETWORK_SUBNET = "172.18.0.0/16"
NETWORK_GATEWAY = "172.18.0.1"
NETWORK_NAME = "toy_net"
CORE_IMAGE = "toy:0.1"
HTTP_IMAGE = "spinner:0.1"
CORE_DOCKER_RPC_PORT = 9876
HTTP_PORT = 8000
HOST_BOUNDED_PORT = 8000


def setup_env():
    os.makedirs(ENV_DIR, exist_ok=True)
    os.makedirs(CORE_ENV_DIR, exist_ok=True)
    os.makedirs(HTTP_ENV_DIR, exist_ok=True)
    # os.makedirs(CORE_PATH, exist_ok=True)
    # os.makedirs(HTTP_PATH, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
