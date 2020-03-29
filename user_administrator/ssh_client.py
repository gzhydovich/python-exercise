import paramiko, socket, sys


def create_user(host, key_filename, new_user, username):
        ssh = ssh_session(host, key_filename, username)

        print("Creating user: " + new_user)
        _, stdout, stderr = ssh.exec_command('sudo useradd ' + new_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stderr) != 0:
                print(decoded_stderr)
        if len(decoded_stdout) != 0:
            print(decoded_stdout)

        print('Closing connection')
        ssh.close()

def list_users(host, key_filename, username):
        ssh = ssh_session(host, key_filename, username)

        awk_command = "awk -F: \'BEGIN{printf \"%-20s %-20s %-20s\\n\", \"USERNAME:\", \"ID:\", \"NAME:\"}; { printf \"%-20s %-20s %-20s\\n\", $1, $3, $5 }\' /etc/passwd"
        _, stdout, stderr = ssh.exec_command(awk_command)
        decoded_stdout = stdout.read().decode('ascii')
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stderr) != 0:
            print(decoded_stderr)
        if len(decoded_stdout) != 0:
            print(decoded_stdout)

        print('\nClosing connection')
        ssh.close()

def delete_user(host, key_filename, delete_user, username):
        ssh = ssh_session(host, key_filename, username)

        print("Deleting user: " + delete_user)
        _, stdout, stderr = ssh.exec_command('sudo userdel ' + delete_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stderr) != 0 :
            print(decoded_stderr)
        if len(decoded_stdout) != 0:
            print(decoded_stdout)

        print('Closing connection')
        ssh.close()

def ssh_session(host, key_filename, username):
    try:
        rsa_key = paramiko.RSAKey.from_private_key_file(key_filename)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, pkey=rsa_key, username=username)
        print("Connected to Server:", host, "User:", username)
        return ssh
    except paramiko.AuthenticationException:
        sys.exit("Error: Authentication problem - Server: " + host + " User: " + username)
    except socket.error as e:
        print("Error: Comunication problem - Server: " + host + " User: " + username)
        sys.exit(e)
