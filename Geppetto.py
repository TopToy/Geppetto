import subprocess
from sys import stdout

import cli

if __name__ == '__main__':
    cli.main()
    # while True:
    #     cmd = input('gep-cli> ')
    #     if cmd == 'exit':
    #         print('Goodbye')
    #         break
    #     subprocess.call(['python', 'cli.py', cmd], stdout=stdout)
