import paramiko, os, string, pprint, socket, traceback, sys

def create_user(host, key_filename, current_user):
    rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
    ssh = paramiko.SSHClient()
    try:
        ssh.connect(host, pkey=rsa_key, username=current_user)
        print("Connected to Server: ", host, "User: ", current_user)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
        print("Result")
        print(ssh_stdout.read())
        print("Errors")
        print(ssh_stderr.read())
    except paramiko.AuthenticationException:
        print("Authentication problem - Server: ", host, "User: ", current_user)
    except socket.error:
        print("Comunication problem - Server: ", host, "User: ", current_user)
    ssh.close()

def list_users(host, key_filename, username):
    rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
    ssh = paramiko.SSHClient()

    ssh.connect(host, pkey=rsa_key)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    print("Result")
    print(ssh_stdout.read())
    print("Errors")
    print(ssh_stderr.read())

def delete_user(host, key_filename, username):
    rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
    ssh = paramiko.SSHClient()

    ssh.connect(host, pkey=rsa_key)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    print("Result")
    print(ssh_stdout.read())
    print("Errors")
    print(ssh_stderr.read())