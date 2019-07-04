#!/usr/bin/env bash

#install python
apt-get update
apt-get install python3-pip

#install java
apt-get install default-jdk
apt-get install maven

#install docker
apt-get remove docker docker-engine docker.io containerd runc
apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get install docker-ce docker-ce-cli containerd.io
groupadd docker
usermod -aG docker $USER

#install docker compose
curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

#install dependecies
pip3 install -r requirements.txt --user

read -p 'We need to restart your system, restart nwo? (y/n): ' answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    reboot
else
    echo "Restart your system before running Geppetto"
fi
