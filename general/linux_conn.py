"""
check migration status of a web service with given set of hosts and port_A, port_B

"""

import socket

def migration_status(host, port_A, port_B):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    result = []
    try:
        s.connect((host, port_A))
        s.close()
        result.append(str(port_A))
    except socket.error:
        pass
    try:
        s.connect((host, port_B))
        s.close()
        result.append(str(port_B))
    except socket.error:
        pass
    if len(result) > 0:
        return host +":  " + ",".join(result)
    else:
        return "disconnected"
        

hosts = ['google.com', 'fb.com', 'yahoo.com']
for host in hosts:
    print migration_status(host, 80, 200)
