import paramiko, socket, sys

def create_user(args):
        ssh = ssh_session(args)

        print("Creating user: " + args.new_user)
        _, stdout, stderr = ssh.exec_command('sudo useradd ' + args.new_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stderr) != 0:
                print(decoded_stderr)
        if len(decoded_stdout) != 0:
            print(decoded_stdout)

        print('Closing connection')
        ssh.close()

def list_users(args):
        ssh = ssh_session(args)

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

def delete_user(args):
        ssh = ssh_session(args)

        print("Deleting user: " + args.delete_user)
        _, stdout, stderr = ssh.exec_command('sudo userdel ' + args.delete_user)
        decoded_stdout = stdout.read().decode('ascii').strip("\n")
        decoded_stderr = stderr.read().decode('ascii').strip("\n")
        if len(decoded_stderr) != 0 :
            print(decoded_stderr)
        if len(decoded_stdout) != 0:
            print(decoded_stdout)

        print('Closing connection')
        ssh.close()

def ssh_session(args):
    try:
        rsa_key = paramiko.RSAKey.from_private_key_file(args.ssh_key)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(args.host, pkey=rsa_key, username=args.username)
        print("Connected to Server:", args.host, "User:", args.username)
        return ssh
    except paramiko.AuthenticationException:
        sys.exit("Error: Authentication problem - Server: " + args.host + " User: " + args.username)
    except socket.error as e:
        print("Error: Comunication problem - Server: " + args.host + " User: " + args.username)
        sys.exit(e)
