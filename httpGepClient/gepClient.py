import requests
from termcolor import colored

from settings import BASE_URL


def height(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/height')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return -1
    return int(response.json()['num'])


def liveness(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/liveness')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.text


def pool_size(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/pool_size')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return -1
    return int(response.json()['num'])


def pending_size(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/pending_size')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return -1
    return int(response.json()['num'])


def validators(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/validators')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(requests.status_codes), 'red'))
        return ''
    return response.json()['ips']


def info(port, ip='127.0.0.1'):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) + 'state/info')
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()


def get_tx(port,ip, c, w, p, b, t, blocking=0):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) +
                            'transactions/cid={}&worker={}&pid={}&bid={}&tx_num={}&blocking={}'
                            .format(c, w, p, b, t, blocking))
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()

def get_tx_data(port,ip, c, w, p, b, t, blocking=0):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) +
                            'transactions/cid={}&worker={}&pid={}&bid={}&tx_num={}&blocking={}/data'
                            .format(c, w, p, b, t, blocking))
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()


def tx_status(port,ip, c, w, p, b, t):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) +
                            'transactions/cid={}&worker={}&pid={}&bid={}&tx_num={}/status'
                            .format(c, w, p, b, t))
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()['status']


def get_block(port,ip, c, h, blocking=0):
    response = requests.get(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) +
                            'blocks/cid={}&height={}&blocking={}'
                            .format(c, h, blocking))
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()


def write_tx(port,ip, c, data):
    response = requests.post(BASE_URL.replace('[ip]:[port]', '{}:{}'.format(ip, port)) +
                            'transactions/cid={}?data={}'.format(c, data))#, data={'data': data})
    if response.status_code != 200:
        print(colored('Unsuccessful call, code {}'.format(response.status_code), 'red'))
        return ''
    return response.json()
