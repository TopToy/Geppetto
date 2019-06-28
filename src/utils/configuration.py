import os

from settings import ENV_DIR, CLUSTER_SIZE, POSSIBLE_FAILURES, WORKERS, INIT_TMO, BLOCK_SIZE


def generate_core_toml():
    os.makedirs(ENV_DIR, exist_ok=True)
    toml = open(os.path.join(ENV_DIR, 'config.toml'), "w+")
    toml.write(
'title = "configuration"\n\
[system]\n\
    \tn = {}\n\
    \tf = {}\n\
    \tc = {}\n\
    \ttesting = false\n\
    \ttxSize = 0\n\
[setting]\n\
    \ttmo = {}\n\
    \tABConfigPath = "src/main/resources/ABConfig"\n\
    \tmaxTransactionInBlock = {}\n\
    \tcaRootPath = ""\n\
[server]\n\
    \tprivateKey = """MIGNAgEAMBAGByqGSM49AgEGBSuBBAAKBHYwdAIBAQQg/ngTdAL+eZOyh4lilm6djqsl\n\
                    RDHT5C60eLxRcEoNjAGgBwYFK4EEAAqhRANCAASeFQqtyOwJcJtYceofW2TeNg7rJBlW\n\
                    L28GZn+tk32fz95JqVS3+iF6JdoM1clkRFLliyXSxEnS1iO4wzRKGQwm"""\n\
    \tTlsPrivKeyPath = "src/main/resources/sslConfig/server.pem"\n\
    \tTlsCertPath = "src/main/resources/sslConfig/server.crt"\n\
[[cluster]]'.format(CLUSTER_SIZE, POSSIBLE_FAILURES, WORKERS, INIT_TMO, BLOCK_SIZE)
    )
