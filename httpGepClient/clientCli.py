import ast
from cmd import Cmd

from termcolor import colored

from httpGepClient import gepClient


class GepClient(Cmd):
    prompt = 'gep-client> '
    intro = "Welcome!\n This program is an http interactive client for the TopToy cluster\n" \
            " Type ? to list commands"


    def do_exit(self, args):
        """
        Exit the client.
        """
        return True


    def do_height(self, args):
        """
        Get the current current blockchain height
        :params:
            -ip: The frontend IP (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: The current blockchain height
        """
        try:
            ip, port = get_ip_and_port(args)
            print("Height = {}".format(gepClient.height(port, ip)))
        except Exception as e:
            print(e)
       
    
    
    def do_liveness(self, args):
        """
        Check the liveness of the core server
        :params:
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: A string that indicates that everything is good
        """
        try:
            ip, port = get_ip_and_port(args)
            print(colored(gepClient.liveness(port, ip), 'blue'))
        except Exception as e:
            print(e)
        
    
    
    def do_pool_size(self, args):
        """
        Returns the current pool size of the blockchain server
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: The current pool size of the blockchain server
        """
        try:
            ip, port = get_ip_and_port(args)
            print("pool_size = {}".format(gepClient.pool_size(port, ip)))
        except Exception as e:
            print(e)
    
    
    def do_pending_size(self, args):
        """
        Returns the current number of pending requests in the blockchain server
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: The current number of pending requests in the blockchain server
        """
        try:
            ip, port = get_ip_and_port(args)
            print("pending_size = {}".format(gepClient.pending_size(port, ip)))
        except Exception as e:
            print(e)
        
    def do_validators(self, args):
        """
        Returns a ip list of the validators in the cluster
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: A ip list of the validators in the cluster
        """
        try:
            ip, port = get_ip_and_port(args)
            print("validators = {}".format(str(gepClient.validators(port, ip))))
        except Exception as e:
            print(e)
    
    
    def do_info(self, args):
        """
        Returns a general info about the cluster
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
        :return: A general info about the cluster
        """
        try:
            ip, port = get_ip_and_port(args)
            print("info = {}".format(str(gepClient.info(port, ip))))
        except Exception as e:
            print(e)
     
            
    def do_get_tx(self, args):
        """
        Returns a transaction by the supplied arguments
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
            -c: The client ID (mandatory)
            -w: The worker ID (mandatory)
            -p: The proposer ID (mandatory)
            -b: The block ID (mandatory)
            -t: The transaction index (mandatory)
            -bl: Whether to block the call (default is 0 (false))
            Note that -c, -w, -p, -b and -t can be retrieved from the return value of write_tx action
        :return: The transaction with the above arguments
        """
        try:
            ip, port = get_ip_and_port(args)
            bl = get_arg_by_key(args.split(), '-bl')
            if bl is None:
                bl = 0
            print("transaction = {}".format(str(gepClient.get_tx(port, ip, get_c(args),
                                                     get_w(args), get_p(args), 
                                                     get_b(args), get_t(args),
                                                     bl))))
        except Exception as e:
            print(e)

    def do_get_tx_data(self, args):
        """
        Returns a transaction data by the supplied arguments
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
            -c: The client ID (mandatory)
            -w: The worker ID (mandatory)
            -p: The proposer ID (mandatory)
            -b: The block ID (mandatory)
            -t: The transaction index (mandatory)
            -bl: Whether to block the call (default is 0 (false))
            Note that -c, -w, -p, -b and -t can be retrieved from the return value of write_tx action
        :return: The transaction data with the above arguments
        """
        try:
            ip, port = get_ip_and_port(args)
            bl = get_arg_by_key(args.split(), '-bl')
            if bl is None:
                bl = 0
            print("data = {}".format(gepClient.get_tx_data(port, ip, get_c(args),
                                                     get_w(args), get_p(args), 
                                                     get_b(args), get_t(args),
                                                     bl)['data']))
        except Exception as e:
            print(e)


    def do_tx_status(self, args):
        """
        Returns the transaction status by the supplied arguments
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
            -c: The client ID (mandatory)
            -w: The worker ID (mandatory)
            -p: The proposer ID (mandatory)
            -b: The block ID (mandatory)
            -t: The transaction index (mandatory)
            Note that -c, -w, -p, -b and -t can be retrieved from the return value of writeTx action
        :return: The transaction with the above arguments status
        """
        try:
            ip, port = get_ip_and_port(args)
            print("transaction = {}".format(gepClient.tx_status(port, ip, get_c(args),
                                                             get_w(args), get_p(args),
                                                             get_b(args), get_t(args))))
        except Exception as e:
            print(e)


    def do_get_block(self, args):
        """
        Returns a block by the supplied arguments
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
            -c: The client ID (mandatory)
            -h: The block height (mandatory)
            -bl: Whether to block the call (default is 0 (false))
        :return: The a block with the above arguments
        """
        try:
            ip, port = get_ip_and_port(args)
            h = get_arg_by_key(args.split(), '-h')
            if h is None:
                raise Exception("No height was specified")
            bl = get_arg_by_key(args, '-bl')
            if bl is None:
                bl = 0
            print("transaction = {}".format(str(gepClient.get_block(port, ip, get_c(args),
                                                                h, bl))))
        except Exception as e:
            print(e)
            
            
    def do_write_tx(self, args):
        """
        Writes a transaction 
        :params: 
            -ip: The ip of the frontend server (default is 127.0.0.1)
            -port: The frontend port (mandatory)
            -c: The client ID (mandatory)
            -d: The data to write, in string format (mandatory)
        :return: The the written transaction ID.
        """
        try:
            ip, port = get_ip_and_port(args)
            d = get_arg_by_key(args.split(), '-d')
            if d is None:
                raise Exception("No data was provided")
            print("transaction ID = {}".format(str(gepClient.write_tx(port, ip, get_c(args), d))))
        except Exception as e:
            print(e)
            

def get_arg_by_key(args, key):
    if key not in args:
        return None
    return args[args.index(key) + 1]


def get_ip_and_port(args):
    args1 = args.split()
    ip = get_arg_by_key(args1, '-ip')
    port = get_arg_by_key(args1, '-port')
    if port is None:
        raise Exception("No port was specified")
    if ip is None:
        ip = '127.0.0.1'
    return ip, port


def get_c(args):
    args1 = args.split()
    c = get_arg_by_key(args1, '-c')
    if c is None:
        raise Exception("No cid was specified")
    return c
    
    
def get_w(args):
    args1 = args.split()
    w = get_arg_by_key(args1, '-w')
    if w is None:
        raise Exception("No worker was specified")
    return w
 
    
def get_p(args):
    args1 = args.split()
    p = get_arg_by_key(args1, '-p')
    if p is None:
        raise Exception("No pid was specified")
    return p
    
    
def get_b(args):
    args1 = args.split()
    b = get_arg_by_key(args1, '-b')
    if b is None:
        raise Exception("No bid was specified")
    return b
    
    
def get_t(args):
    args1 = args.split()
    t = get_arg_by_key(args1, '-t')
    if t is None:
        raise Exception("No tx_num was specified")
    return t
    
 
def main_cli():
    GepClient().cmdloop()
