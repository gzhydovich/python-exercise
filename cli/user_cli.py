import argparse
import getpass

from .ssh_client import SSHClient

parser = argparse.ArgumentParser(description="Helps with administration of users on a specified host")
subparsers = parser.add_subparsers(
    dest='command',
    help='Commands',
    required=True,
)

# Create
parser_create = subparsers.add_parser('create', help='Creates a user on a specified host')
parser_create.add_argument(
    "--host",
    help="Host address",
    type=str, 
    required=True,
)
parser_create.add_argument(
    "--ssh-key",
    help="Path to SHH key file",
    type=str,
    required=True,
)
parser_create.add_argument(
    "--new-user",
    help='User to be created',
    type=str,
    required=True,
)
parser_create.add_argument(
    "--username",
    help="Specific user for the ssh session, if different from the active user",
    type=str,  
)

# List
parser_list = subparsers.add_parser('list', help='Returns a list of users on a specified host')
parser_list.add_argument(
    "--host",
    help="Host address",
    type=str, 
    required=True,
)
parser_list.add_argument(
    "--ssh-key",
    help="Path to SHH key file",
    type=str,
    required=True,
)
parser_list.add_argument(
    "--username",
    help="Specific user for the ssh session, if different from the active user",
    type=str,  
)

# Delete
parser_delete = subparsers.add_parser('delete', help='Deletes a user on a specified host')
parser_delete.add_argument(
    "--host",
    help="Host address",
    type=str, 
    required=True,
)
parser_delete.add_argument(
    "--ssh-key",
    help="Path to SHH key file",
    type=str,
    required=True,
)
parser_delete.add_argument(
    "--delete-user", "-du",
    help='User to be deleted',
    type=str,
    required=True,
)
parser_delete.add_argument(
    "--username",
    help="Specific user for the ssh session, if different from the active user",
    type=str,  
)

args = parser.parse_args()
if not args.username:
    args.username = getpass.getuser()

client = SSHClient(args)
if args.command == "create":
    client.create_user()
if args.command == "list":
    client.list_users()
if args.command == "delete":
    client.delete_user()