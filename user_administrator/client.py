import paramiko



def create_user(host, ):
    ssh = paramiko.SSHClient()
    
    ssh.connect(host, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
    raise NotImplementedError