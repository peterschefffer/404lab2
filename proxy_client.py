import socket

BTYES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost" + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    res = s.recv(BTYES_TO_READ)
    final = b'' + res

    while(len(res) > 0):
        res = s.recv(BTYES_TO_READ)
        final += res
    s.close()
    return final

print(get('127.0.0.1', 8080))