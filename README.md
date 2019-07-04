# Geppetto
A deployer for a docker based TopToy network

## Installation
1. Install necessary tools (such as python3, java, docker and maven):
    ```bash
    cd path/to/Geppetto
    sudo ./install.sh
    ```
## Example
The following deploys a basic TopToy network with a single core server and a single frontend server 
```bash
./Geppetto.py setup
./Geppetto.py run    
```
The frontend is accessible at 127.0.0.1:8000 and may negotiated by a RESTful API
 as described in the [Spinner](https://github.com/TopToy/Spinner.git) project.

To reconfigure the cluster, go to `settings.py` and edit it as you wish.
To stop the network, run:
```bash
./Geppetto.py stop
```

To clean all generated resources, run:
```bash
./Geppetto.py clean
```

To get a full elaboration of Geppetto commands, type:
```bash
./Geppetto.py --help
```

## Geppetto Client
Geppetto has an http client interactive shell.

To run the client shell type
```bash
./Gepptto.py client
```
press `?` to see the possible commands.



