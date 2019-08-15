import socket

def is_connection_ok():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)
    try:
        client.connect(('google.com', 80))
        
        #print(client.recv(1024))
        return True
    except socket.error as e:
        print(e)
        return False
    finally:
        client.close()

def get_ip(host):
    try:
        return socket.gethostbyname(host)
    except:
        return 'INVALID_HOST_NAME'

def get_tld_server(tld="com"):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("whois.iana.org", 43))
    client.send("{}\n".format(tld).encode("utf-8"))
    for line in client.makefile():
        parts = line.split(":", 2)
        if len(parts) > 1:
            header_name = parts[0].strip()
            header_value = parts[1].strip()
            if header_name.lower() == "whois":
                return header_value
                
def who_is(host, server=None):
    if not server:
        tld = host.split(".")[-1]
        server = get_tld_server(tld)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.settimeout(2)

    client.connect((server, 43)) # Passive open

    client.send("{}\n".format(host).encode("utf-8"))
    for line in client.makefile():
        part_lines = line.split(':', 2)
        if len(part_lines) > 1:
            yield part_lines[1].replace('\n', '')




#print(is_connection_ok())

# print(who_is('neucentrix.co.id'))
print(next(who_is('neucentrix.co.id')))