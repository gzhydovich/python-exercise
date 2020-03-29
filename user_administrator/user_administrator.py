import argparse
import getpass
from .ssh_client import create_user, list_users, delete_user

def create_user_middleman(args):
    create_user(host=args.host, key_filename=args.ssh_key, new_user=args.new_user, username=args.username)

def list_users_middleman(args):
    print('"list()" called')
    print(args)


def delete_user_middleman(args):
    delete_user(host=args.host, key_filename=args.ssh_key, delete_user=args.delete_user, username=args.username)


parser = argparse.ArgumentParser(description="Helps with administration of users on a specified host")
subparsers = parser.add_subparsers(dest='create/list/delete', required=True, help='Comands')

# Create
parser_create = subparsers.add_parser('create', help='Creates a user on a specified host')
parser_create.set_defaults(func=create_user_middleman)
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
parser_list.set_defaults(func=list_users_middleman)
parser_create.add_argument("--host",
                            type=str, 
                            required=True,
                            help="Host address")
parser_create.add_argument("--ssh-key",
                            type=str,
                            required=True,
                            help="SHH key file")
parser_create.add_argument("--username",
                            type=str,  
                            help="Specific user for the ssh session, if different from the active user")
# think of verbose output

# Delete
parser_delete = subparsers.add_parser('delete', help='Deletes a user on a specified host')
parser_delete.set_defaults(func=delete_user_middleman)
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

# type=argparse.FileType('r')
# with args.sshkey as f:
#     print(f.read())
# print args.file.readlines()



