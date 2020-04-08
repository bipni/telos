import socket

class MyIP:

    @staticmethod
    def get_ip():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        host = "8.8.8.8"
        port = 80

        sock.connect((host, port))

        ip = sock.getsockname()[0]

        sock.close()

        return ip

def run():
    return MyIP.get_ip()