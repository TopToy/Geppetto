# Geppetto
A deployer for a docker based TopToy network

## Installation
1. Install Python3.7
    ```bash
    sudo apt-get update
    sudo apt-get install python3.7
    ```
1. Install dependencies
    ```bash
    pip install -r requirements.txt
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
python Gepptto client
```
press `?` to see the possible commands.



