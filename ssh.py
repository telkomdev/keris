from common import is_connection_ok
import paramiko

"""
execute_ssh(host, port, username, password, cmd)
"""
def execute_ssh(host, username, password, cmd, port='22'):
    if is_connection_ok():
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=int(port), username=username, password=password)
            _, stdout, stderr = ssh.exec_command(cmd, timeout=5)
            res = stdout.read().decode()

            error = stderr.read().decode('utf-8')
            if error:
                print(error)
                return 'SSH_CONNECTION_FAIL'
            else:
                ssh.close()
                return 'SSH_CONNECTION_SUCCESS with username : {username} and password {password}'.format(username=username, password=password)
        except Exception:
            print('*')
            return 'SSH_CONNECTION_FAIL'
    else:
        return 'CONNECTION_NOT_FOUND'
        
res = execute_ssh('128.199.204.131', 'devuser', 'Rkht34$.Hkq9lsi%rt1', 'pwd', '2217')
print(res)