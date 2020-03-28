import argparse
# import user_administrator.client


def create_user(args):
    print('"creaate()" called')
    print(args.sshkey.read())

def list_users(args):
    print('"list()" called')
    print(args.sshkey.read())

def delete_user(args):
    print('"delete()" called')
    # print(args.sshkey.read())
    print(args.sshkey)


parser = argparse.ArgumentParser(description="Helps with administration of users on a specified host")
subparsers = parser.add_subparsers(dest='create/list/delete', required=True, help='Comands')

# Create
parser_create = subparsers.add_parser('create', help='Creates a user on a specified host')
parser_create.set_defaults(func=create_user)
parser_create.add_argument("--host", type=str, required=True, help="Host address")
parser_create.add_argument("--sshkey", type=str, required=True, help="SHH key file")
parser_create.add_argument("--user-name", type=str, required=True, help='User to be created')

# List
parser_list = subparsers.add_parser('list', help='Returns a list of users on a specified host')
parser_list.set_defaults(func=list_users)
parser_list.add_argument("--host", type=str, required=True, help="Host address")
parser_list.add_argument("--sshkey", type=str, required=True, help="SHH key file")

# Delete
parser_delete = subparsers.add_parser('delete', help='Deletes a user on a specified host')
parser_delete.set_defaults(func=delete_user)
parser_delete.add_argument("--host", type=str, required=True, help="Host address")
parser_delete.add_argument("--sshkey", type=argparse.FileType('r'), required=True, help="SHH key file")


args = parser.parse_args()

if not args.host:
    parser.error('Host has to be provided')

args.func(args)


# with args.sshkey as f:
#     print(f.read())
# 
# print args.file.readlines()



