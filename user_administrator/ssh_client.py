import paramiko, socket, sys

def create_user(host, key_filename, new_user, username):
    try:
        rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, pkey=rsa_key, username=username)

        print("Connected to Server:", host, "User:", username)
        print("Creating user: " + new_user)

        stdin, stdout, stderr = ssh.exec_command('sudo useradd ' + new_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stdout) != 0:
            print("Result: " + decoded_stdout)
        if len(decoded_stderr) != 0:
            print("Error: " + decoded_stderr)
        print('Closing connection')
        ssh.close()
    except paramiko.AuthenticationException:
        sys.exit("Error: Authentication problem - Server: " + host + " User: " + username)
    except socket.error:
        sys.exit("Error: Comunication problem - Server: " + host + " User: " + username)

def list_users(host, key_filename, username):
    try:
        rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, pkey=rsa_key, username=username)
        print("Connected to Server:", host, "User:", username)

        stdin, stdout, stderr = ssh.exec_command('sudo less /etc/passwd ')
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stdout) != 0:
            print("Result:\n" + decoded_stdout)
        if len(decoded_stderr) != 0:
            print("Error: " + decoded_stderr)
        print('Closing connection')
        ssh.close()
    except paramiko.AuthenticationException:
        sys.exit("Error: Authentication problem - Server: " + host + " User: " + username)
    except socket.error:
        sys.exit("Error: Comunication problem - Server: " + host + " User: " + username)

def delete_user(host, key_filename, delete_user, username):
    try:
        rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(host, pkey=rsa_key, username=username)
        print("Connected to Server:", host, "User:", username)
        print("Deleting user: " + delete_user)
        stdin, stdout, stderr = ssh.exec_command('sudo userdel ' + delete_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stdout) != 0:
            print("Result: " + decoded_stdout)
        if len(decoded_stderr) != 0:
            print("Error: " + decoded_stderr)
        print('Closing connection')
        ssh.close()
    except paramiko.AuthenticationException:
        sys.exit("Error: Authentication problem - Server: " + host + " User: " + username)
    except socket.error:
        sys.exit("Error: Comunication problem - Server: " + host + " User: " + username)

def client_setup(host, key_filename, username):
    rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, pkey=rsa_key, username=username)
    print("Connected to Server:", host, "User:", username)
    return ssh