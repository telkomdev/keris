import socket
from colors import give_color
from common import is_connection_ok, get_ip

"""
scan_ports(host, from_port, to_port)
params:
   - host
   - from port
   - to port
"""
def scan_ports(host, from_port, to_port):
    if is_connection_ok():
        ip_res = get_ip(host)

        if ip_res == 'INVALID_HOST_NAME':
            return 'INVALID_HOST_NAME'
        else:
            if from_port <= to_port:
                
                for port in range(from_port, to_port):
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)

                    print(give_color(' Scanning PORT {}'.format(port), 'cyan'))

                    result = client.connect_ex((ip_res, port))
                    if result == 0:
                        print(give_color('PORT {} is open'.format(port), 'cyan'))
                    client.close()
                return "DONE"

    else:
        return 'CONNECTION_NOT_FOUND'