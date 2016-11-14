import socket
import ssl
import binascii
import time
from hpack.hpack import Encoder, Decoder

SERVER_PREFACE = b'\x00\x00\x00\x04\x01\x00\x00\x00\x00'


def server_start(socket):
    print('Hi I\'m server')
    socket.bind(('127.0.0.1', 50000))
    socket.listen(5)
    while True:
        try:
            conn, addr = socket.accept()
            data = conn.recv(1024)
            print(binascii.hexlify(data))
            print(data)
            print(len(data))
            print('='*50)
            if len(data) == 0:
                break
            send_preface(conn)
            print('='*50)
            data = conn.recv(1024)
            print(binascii.hexlify(data))
            print(data)
            print(len(data))
            print('---------------')
            conn.send(b'\x00\x00\x00\x04\x01\x00\x00\x00\x00')
            data = conn.recv(1024)
            print(binascii.hexlify(data))
            print(data)
            print(len(data))
            print('---------------')

            data = conn.recv(1024)
            print(binascii.hexlify(data))
            # print(data)
            print(len(data))
            print('---------------')
        except KeyboardInterrupt:
            conn.close()
            print("ERROR!")
            break

def send_preface(socket):
    print("asdasd")


if __name__ == '__main__':
    if hasattr(ssl, 'SSLContext'):
        if hasattr(ssl, 'PROTOCOL_TLSv1_2'):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        else:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            print("TLSv1")

        protocol_nego = None
        if hasattr(ssl, 'HAS_NPN'):
            if ssl.HAS_NPN:
                protocol_nego = 'NPN'
                ssl_context.set_npn_protocols(['h2'])
        if hasattr(ssl, 'HAS_ALPN'):
            if ssl.HAS_ALPN:
                protocol_nego = 'ALPN'
                ssl_context.set_alpn_protocols(['h2'])

        if protocol_nego is None:
            print('[INFO] Unsupport NPN or ALPN')

        ssl_context.load_cert_chain(
            certfile='./server.crt',
            keyfile='./server.key'
        )

        listen_sock = ssl_context.wrap_socket(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM),
            server_side=True
        )
        server_start(listen_sock)
