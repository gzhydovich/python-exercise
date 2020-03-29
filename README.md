# SSH USER CLI

## Prerequisites
Python 3.8
pip

## Getting started
`python -m pip install --user -e .`


## Usage
```bash
$ python3 -m cli.user_cli -h
usage: user_cli.py [-h] {create,list,delete} ...

Helps with administration of users on a specified host

positional arguments:
  {create,list,delete}  Commands
    create              Creates a user on a specified host
    list                Returns a list of users on a specified host
    delete              Deletes a user on a specified host
```

## Examples

* CREATE
```bash
$ python3 -m cli.user_cli create --host example.us-east-2.compute.amazonaws.com --ssh-key example.pem --user ec2-user --new-user gene-120
Connected to Server: example.compute.amazonaws.com User: ec2-user
Creating user: gene-120
Closing connection
```

* LIST
```bash
$ python3 -m cli.user_cli list --host example.us-east-2.compute.amazonaws.com --ssh-key example.pem --user ec2-user
Connected to Server: example.compute.amazonaws.com User: ec2-user
USERNAME:            ID:                  NAME:
root                 0                    root
bin                  1                    bin
daemon               2                    daemon
...
...
gene-4               504


Closing connection
```

* DELETE
```bash
$ python -m cli.user_cli delete --host example.us-east-2.compute.amazonaws.com --ssh-key example.pem --user ec2-user --delete-user gene-120
Connected to Server: example.us-east-2.compute.amazonaws.com User: ec2-user
Deleting user: gene-120
Closing connection
```