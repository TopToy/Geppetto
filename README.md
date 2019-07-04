# Geppetto
A deployer for a docker based TopToy network

## Installation
1. Install Python3.7
    ```bash
    sudo apt-get update
    sudo apt-get install python3.7
    ```
1. Install pip3
    ```bash
    sudo apt-get install python3-pip
    ```
1. Install dependencies
    ```bash
    pip3 install -r requirements.txt
    ```
1. Install Java
    ```
    sudo apt update
    sudo apt install default-jdk
    ```
1. Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
    1. Remove an old version (if exists)
        ```
        sudo apt-get remove docker docker-engine docker.io containerd runc
        ```
    1. Set Up The Repository
        ```
        sudo apt-get update
        sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo apt-key fingerprint 0EBFCD88
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        ```
    1. Install Docker
        ```
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        ```
    1. Add permissions for your current user to run docker
        ```
        sudo groupadd docker
        sudo usermod -aG docker $USER
        ```
    1. Restart (or logout and login) your system
    1. Install docker-compose
        ```
        sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
        ```
1. Install [maven](https://maven.apache.org/install.html)
    ```
    sudo apt update
    sudo apt install maven
    ```

## Example
The following deploys a basic TopToy network with a single core server and a single frontend server 
```bash
python Geppetto.py setup
python Geppetto.py run    
```
The frontend is accessible at 127.0.0.1:8000 and may negotiated by a RESTful API
 as described in the [Spinner](https://github.com/TopToy/Spinner.git) project.

To reconfigure the cluster, go to `settings.py` and edit it as you wish.
To stop the network, run:
```bash
python Geppetto.py stop
```

To clean all generated resources, run:
```bash
python Geppetto.py clean
```

To get a full elaboration of Geppetto commands, type:
```bash
python Geppetto.py --help
```

## Geppetto Client
Geppetto has an http client interactive shell.

To run the client shell type
```bash
python Gepptto.py client
```
press `?` to see the possible commands.



