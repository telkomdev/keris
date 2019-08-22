import socket
import re

"""
is_connection_ok()

check internet connection, return True if connection was ok
return boolean
"""
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

"""
get_ip(host)

params domain, eg: get_ip('www.example.com')
return ip address
"""
def get_ip(host):
    try:
        return socket.gethostbyname(host)
    except:
        return 'INVALID_HOST_NAME'

"""
return whois with its suffix
"""
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

"""
who_is(host)

params domain, eg: who_is('www.example.com')
return whois data
"""        
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




# print(is_connection_ok())

# print(who_is('neucentrix.co.id'))
# print(next(who_is('neucentrix.co.id')))

"""
is_valid_url(host)
"""
def is_valid_url(host):
    regex = re.compile(
        r'^(?:http|ftp)s?://|' # http:// or https:// or
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, host) is not None

#print(is_valid_url('http://wuriyanto.com'))