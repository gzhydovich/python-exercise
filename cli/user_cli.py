import argparse
import getpass
from .ssh_client import create_user, list_users, delete_user

parser = argparse.ArgumentParser(description="Helps with administration of users on a specified host")
subparsers = parser.add_subparsers(dest='create/list/delete', required=True, help='Comands')

# Create
parser_create = subparsers.add_parser('create', help='Creates a user on a specified host')
parser_create.set_defaults(func=create_user)
parser_create.add_argument("--host",
                            type=str, 
                            required=True,
                            help="Host address")
parser_create.add_argument("--ssh-key",
                            type=str,
                            required=True,
                            help="SHH key file")
parser_create.add_argument("--new-user", "-nu",
                            type=str,
                            required=True,
                            help='User to be created')
parser_create.add_argument("--username",
                            type=str,  
                            help="Specific user for the ssh session, if different from the active user")

# List
parser_list = subparsers.add_parser('list', help='Returns a list of users on a specified host')
parser_list.set_defaults(func=list_users)
parser_list.add_argument("--host",
                            type=str, 
                            required=True,
                            help="Host address")
parser_list.add_argument("--ssh-key",
                            type=str,
                            required=True,
                            help="SHH key file")
parser_list.add_argument("--username",
                            type=str,  
                            help="Specific user for the ssh session, if different from the active user")
# think of verbose output

# Delete
parser_delete = subparsers.add_parser('delete', help='Deletes a user on a specified host')
parser_delete.set_defaults(func=delete_user)
parser_delete.add_argument("--host",
                            type=str, 
                            required=True,
                            help="Host address")
parser_delete.add_argument("--ssh-key",
                            type=str,
                            required=True,
                            help="SHH key file")
parser_delete.add_argument("--delete-user", "-du",
                            type=str,
                            required=True,
                            help='User to be deleted')
parser_delete.add_argument("--username",
                            type=str,  
                            help="Specific user for the ssh session, if different from the active user")

args = parser.parse_args()

if not args.username:
    args.username = getpass.getuser()

args.func(args)
