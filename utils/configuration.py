import os

from settings import *

from shutil import copy2
from distutils.dir_util import copy_tree

from utils.utils import create_ip


def generate_core_toml():
    print(">>> Generate config.toml")
    os.makedirs(os.path.join(CORE_ENV_DIR), exist_ok=True)
    toml = open(os.path.join(CORE_ENV_DIR, 'config.toml'), "w+")
    toml.write(
'title = "configuration"\n\
[system]\n\
    n = {}\n\
    f = {}\n\
    c = {}\n\
    testing = false\n\
    txSize = 0\n\
[setting]\n\
    tmo = {}\n\
    ABConfigPath = "src/main/resources/ABConfig"\n\
    maxTransactionInBlock = {}\n\
    caRootPath = ""\n\
[server]\n\
    privateKey = """MIGNAgEAMBAGByqGSM49AgEGBSuBBAAKBHYwdAIBAQQg/ngTdAL+eZOyh4lilm6djqsl\n\
                    RDHT5C60eLxRcEoNjAGgBwYFK4EEAAqhRANCAASeFQqtyOwJcJtYceofW2TeNg7rJBlW\n\
                    L28GZn+tk32fz95JqVS3+iF6JdoM1clkRFLliyXSxEnS1iO4wzRKGQwm"""\n\
    TlsPrivKeyPath = "src/main/resources/sslConfig/server.pem"\n\
    TlsCertPath = "src/main/resources/sslConfig/server.crt"\n\
[[cluster]]\n'.format(CLUSTER_SIZE, POSSIBLE_FAILURES, WORKERS, INIT_TMO, BLOCK_SIZE)
    )
    for i in range(CLUSTER_SIZE):
        toml.write(
'   [cluster.s{}]\n\
        id = {}\n\
        ip = "{}"\n\
        wrbPort = {}\n\
        commPort = {}\n\
        obbcPort = {}\n\
        publicKey ="""MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEnhUKrcjsCXCbWHHqH1tk3jYO6yQZVi9vBmZ/rZ\n\
                   N9n8/eSalUt/oheiXaDNXJZERS5Ysl0sRJ0tYjuMM0ShkMJg=="""\n'
            .format(i, i, create_ip(NETWORK_SUBNET, i + 3), WRB_PORT, COMM_PORT, OBBC_PORT)
    )
    toml.close()


def generate_core_hosts():
    print(">>> Generate hosts.config")
    os.makedirs(os.path.join(CORE_ENV_DIR, 'ABConfig'), exist_ok=True)
    hosts = open(os.path.join(CORE_ENV_DIR, 'ABConfig', 'hosts.config'), "w+")
    hosts.write(
'# Copyright (c) 2007-2013 Alysson Bessani, Eduardo Alchieri, Paulo Sousa, and the authors indicated in the @author tags\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the "License");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
# http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an "AS IS" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
# This file defines the replicas ids, IPs and ports.\n\
# It is used by the replicas and clients to find connection info\n\
# to the initial replicas.\n\
# The ports defined here are the ports used by clients to communicate\n\
# with the replicas. Additional connections are opened by replicas to\n\
# communicate with each other. This additional connection is opened in the\n\
# next port defined here. For an example, consider the line "0 127.0.0.1 11000".\n\
# That means that clients will open a communication channel to replica 0 in\n\
# IP 127.0.0.1 and port 11000. On startup, replicas with id different than 0\n\
# will open a communication channel to replica 0 in port 11001.\n\
# The same holds for replicas 1, 2, 3 ... N.\n\
\n\
#server id, address and port (the ids from 0 to n-1 are the service replicas)\n'
    )
    for i in range(CLUSTER_SIZE):
        hosts.write('{} {} {}\n'.format( i, create_ip(NETWORK_SUBNET, i + 3), AB_PORT))

    hosts.close()


def generate_core_system():
    print(">>> Generate system.config")
    os.makedirs(os.path.join(CORE_ENV_DIR, 'ABConfig'), exist_ok=True)
    sys = open(os.path.join(CORE_ENV_DIR, 'ABConfig', 'system.config'), "w+")
    sys.write(
'# Copyright (c) 2007-2013 Alysson Bessani, Eduardo Alchieri, Paulo Sousa, and the authors indicated in the @author tags\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the "License");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
# http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an "AS IS" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
############################################\n\
####### Communication Configurations #######\n\
############################################\n\
\n\
#HMAC algorithm used to authenticate messages between processes (HmacMD5 is the default value)\n\
#This parameter is not currently being used being used\n\
#system.authentication.hmacAlgorithm = HmacSHA1\n\
\n\
#Specify if the communication system should use a thread to send data (true or false)\n\
system.communication.useSenderThread = true\n\
\n\
#Force all processes to use the same public/private keys pair and secret key. This is useful when deploying experiments\n\
#and benchmarks, but must not be used in production systems.\n\
system.communication.defaultkeys = false\n\
\n\
############################################\n\
### Replication Algorithm Configurations ###\n\
############################################\n\
\n\
#Number of servers in the group\n\
system.servers.num = {}\n\
\n\
#Maximum number of faulty replicas\n\
system.servers.f = {}\n\
\n\
#Timeout to asking for a client request\n\
system.totalordermulticast.timeout = 2000\n\
\n\
\n\
#Maximum batch size (in number of messages)\n\
system.totalordermulticast.maxbatchsize = 400\n\
\n\
#Number of nonces (for non-determinism actions) generated\n\
system.totalordermulticast.nonces = 10\n\
\n\
#if verification of leader-generated timestamps are increasing\n\
#it can only be used on systems in which the network clocks\n\
#are synchronized\n\
system.totalordermulticast.verifyTimestamps = false\n\
\n\
#Quantity of messages that can be stored in the receive queue of the communication system\n\
system.communication.inQueueSize = 500000\n\
\n\
# Quantity of messages that can be stored in the send queue of each replica\n\
system.communication.outQueueSize = 500000\n\
\n\
#Set to 1 if SMaRt should use signatures, set to 0 if otherwise\n\
system.communication.useSignatures = 1\n\
\n\
#Set to 1 if SMaRt should use MAC\'s, set to 0 if otherwise\n\
system.communication.useMACs = 1\n\
\n\
#Set to 1 if SMaRt should use the standard output to display debug messages, set to 0 if otherwise\n\
system.debug = 0\n\
\n\
#Print information about the replica when it is shutdown\n\
system.shutdownhook = true\n\
\n\
############################################\n\
###### State Transfer Configurations #######\n\
############################################\n\
\n\
#Activate the state transfer protocol (\'true\' to activate, \'false\' to de-activate)\n\
system.totalordermulticast.state_transfer = true\n\
\n\
#Maximum ahead-of-time message not discarded\n\
system.totalordermulticast.highMark = 10000\n\
\n\
#Maximum ahead-of-time message not discarded when the replica is still on EID 0 (after which the state transfer is triggered)\n\
system.totalordermulticast.revival_highMark = 10\n\
\n\
#Number of ahead-of-time messages necessary to trigger the state transfer after a request timeout occurs\n\
system.totalordermulticast.timeout_highMark = 200\n\
\n\
############################################\n\
###### Log and Checkpoint Configurations ###\n\
############################################\n\
\n\
system.totalordermulticast.log = true\n\
system.totalordermulticast.log_parallel = false\n\
system.totalordermulticast.log_to_disk = false\n\
system.totalordermulticast.sync_log = false\n\
\n\
#Period at which BFT-SMaRt requests the state to the application (for the state transfer state protocol)\n\
system.totalordermulticast.checkpoint_period = 1000\n\
system.totalordermulticast.global_checkpoint_period = 120000\n\
\n\
system.totalordermulticast.checkpoint_to_disk = false\n\
system.totalordermulticast.sync_ckp = false\n\
\n\
\n\
############################################\n\
###### Reconfiguration Configurations ######\n\
############################################\n\
\n\
#Replicas ID for the initial view, separated by a comma.\n\
# The number of replicas in this parameter should be equal to that specified in \'system.servers.num\'\n\
system.initial.view = {}\n\
#The ID of the trust third party (TTP)\n\
system.ttp.id = 7002\n\
\n\
#This sets if the system will function in Byzantine or crash-only mode. Set to "true" to support Byzantine faults\n\
system.bft = true\n\
'.format(CLUSTER_SIZE, POSSIBLE_FAILURES, ','.join([str(i) for i in range(CLUSTER_SIZE)]))
    )
    sys.close()


def generate_core_keys():
    print(">>> Generate core keys")
    os.makedirs(os.path.join(CORE_ENV_DIR, 'ABConfig', 'keys'), exist_ok=True)
    for i in range(CLUSTER_SIZE):
        copy2('files/core_files/keys/privatekey',
              os.path.join(CORE_ENV_DIR, 'ABConfig', 'keys', 'privatekey' + str(i)))
        copy2('files/core_files/keys/publickey',
              os.path.join(CORE_ENV_DIR, 'ABConfig', 'keys', 'publickey' + str(i)))


def generate_core_log4j():
    print(">>> Generate core log4j.properties")
    copy2('files/core_files/log4j.properties', CORE_ENV_DIR)


def generate_core_ssl():
    print(">>> Generate core ssl")
    os.makedirs(os.path.join(CORE_ENV_DIR, 'sslConfig'), exist_ok=True)
    copy_tree('files/core_files/ssl', os.path.join(CORE_ENV_DIR, 'sslConfig'))


def config_core_inst():
    print(">>> Generate core instruction")
    os.makedirs(os.path.join(CORE_ENV_DIR, 'inst'), exist_ok=True)
    f = open(os.path.join(CORE_ENV_DIR, 'inst', 'input.inst'), "w+")
    f.write('up\n')
    f.close()


def config_core():
    print(">>> Generate core configuration")
    generate_core_toml()
    generate_core_hosts()
    generate_core_system()
    generate_core_keys()
    generate_core_log4j()
    generate_core_ssl()
    config_core_inst()


def config_tools():
    config_core()
