import os

# Global settings #
CORE_SERVER = 'TopToy'
CORE_GIT_URL = 'https://github.com/TopToy/TopToy.git'
HTTP_SERVER = 'Spinner'
HTTP_GIT_URL = 'https://github.com/TopToy/Spinner.git'
WORKING_DIR = '/tmp/Geppetto_wd'

# Environment settings #
ENV_DIR = os.path.join(WORKING_DIR, 'env')
CORE_ENV_DIR = os.path.join(ENV_DIR, CORE_SERVER)
HTTP_ENV_DIR = os.path.join(ENV_DIR, HTTP_SERVER)
CORE_PATH = os.path.join(WORKING_DIR, CORE_SERVER)
HTTP_PATH = os.path.join(WORKING_DIR, HTTP_SERVER)

# Core deployment settings #
CLUSTER_SIZE = 4
POSSIBLE_FAILURES = 1
WORKERS = 1
BLOCK_SIZE = 1000
INIT_TMO = 100

## Ports
WRB_PORT = 30000
OBBC_PORT = 30010
COMM_PORT = 30020
AB_PORT = 12000

# Docker settings
NETWORK_CIDR = "172.18.0.0/16"
NETWORK_GATEWAY = "172.18.0.1"