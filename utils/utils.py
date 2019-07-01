import os
import subprocess

from settings import CORE_GIT_URL, HTTP_GIT_URL, CORE_PATH, HTTP_PATH
from git import Repo

from utils.dockerUtiles import build_docker_images


def install():
    clone_and_update_repo(CORE_PATH, CORE_GIT_URL)
    clone_and_update_repo(HTTP_PATH, HTTP_GIT_URL)
    compile_core(CORE_PATH)
    compile_core(HTTP_PATH)


def clone_and_update_repo(repo_ptah, repo_url):
    print('>>> Updating {} from {}'.format(repo_ptah, repo_url))
    if not os.path.exists(repo_ptah):
        Repo.clone_from(repo_url, repo_ptah)
    Repo(repo_ptah).remotes['origin'].pull()


def compile_core(project_directory):
    print('>>> Building {}'.format(project_directory))
    subprocess.call(['make', '-C', project_directory, 'build'])


def create_ip(cidr,last_block):
    return (cidr.split('/')[0] + 'r').replace(cidr.split('/')[0].split('.')[-1] + 'r', str(last_block))
