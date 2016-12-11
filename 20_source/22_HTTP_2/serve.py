"""
██╗  ██╗████████╗████████╗██████╗ ██████╗     ███████╗███████╗██████╗  ██╗   ██╗███████╗██████╗
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗╚════██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████║   ██║         ██║    ██████╔╝ █████╔╝    ███████╗█████╗  ██████╔╝ ██║   ██║█████╗  ██████╔╝
██╔══██║   ██║         ██║    ██╔═══╝  ██╔═══╝     ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║   ██║   ██║         ██║    ██║       ███████╗    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝    ╚═╝         ╚═╝    ╚═╝       ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝

한국디지털미디어고등학교 2016학년도 창의IT 공모전 출품작
14기 해킹방어과 박영훈, 차수환

Copyright - MIT
https://github.com/HTTP2Server/HTTP2/blob/master/LICENSE
"""
import socket
import ssl
import binascii
import time
from hpack import Encoder, Decoder

SERVER_PREFACE = b'\x00\x00\x00\x04\x01\x00\x00\x00\x00'

PreSet = {
'HOST' : '127.0.0.1',
'PORT' : 50000
}

# Encoder = Encoder()
# Decoder = Decoder()

develope = 1

id = {
    -1 : 'preface'

}

# Setting Class Start
class setting:
    def RunServer(self):
        print("[INFO]HTTP2 Server START...")
        if hasattr(ssl, 'SSLContext'):
            if hasattr(ssl, 'PROTOCOL_TLSv1_2'):
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                print("[OK]Serving with TLSv1.2")
            else:
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                print("[WARN]Serving with TLSv1")

            protocol_nego = None
            if hasattr(ssl, 'HAS_NPN'):
                if ssl.HAS_NPN:
                    protocol_nego = 'NPN'
                    ssl_context.set_npn_protocols(['h2'])
                    print('[OK] SSL will use NPN')
            if hasattr(ssl, 'HAS_ALPN'):
                if ssl.HAS_ALPN:
                    protocol_nego = 'ALPN'
                    ssl_context.set_alpn_protocols(['h2'])
                    print('[OK] SSL will use APAN')

            if protocol_nego is None:
                print('[ERROR] Server isn\'t support NPN or ALPN')
            while True:
                try:
                    ssl_context.load_cert_chain(
                        certfile='./server.crt',
                        keyfile='./server.key'
                    )
                    break
                except Exception as e:
                    print("[ERROR]",e)
                    continue
            listen_sock = ssl_context.wrap_socket(
                socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                server_side=True
            )
            return listen_sock
        else:
            print('[ERROR]Server DO NOT surpport SSL')
# Setting Class End

# OpenSocekt Start
class OpenSocket():
    def __init__(self,socket):
        self.socket = socket
        self.HOST = PreSet['HOST']
        self.PORT = PreSet['PORT']
    def run(self):
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen(5)
        print('[INFO]Run server at '+self.HOST+':'+str(self.PORT))
        return self.socket
# OpenSocekt End

# class http2 start -> require Threading task(async.io)
class http2():
    def __init__(self, socket):
        self.socket = socket
    def run(self):
        while True:
            try:
                self.conn, self.addr = self.socket.accept()
                while True:
                    try:
                        data = self.conn.recv(1024)
                    except:
                        print("[WARN]Fail to receive data")
                        self.conn.close()
                        break
                    if develope == 1:
                        print('='*50)
                        print(data)
                        print('='*50)

                    if len(data) == 0:
                        print("[ERROR]Receive Data is Empty")
                        break


                    switch {
                        b'\x01' : type_1,    # HEADER
                        b'\x02' : type_2,    # PRIORITY
                        b'\x03' : type_3,    # RST_STREAM
                        b'\x04' : type_4,    # setting
                        b'\x05' : type_5,    # PUSH_PROMISE
                        b'\x06' : type_6,    # PING
                        b'\x07' : type_7,    # GOAWAY
                        b'\x08' : type_8,    # WINDOW_UPDATE
                        b'\x09' : type_9     # CONTINUATION
                    }

                    val = switch.get(data[3:4])


                    if data == b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n':
                        self.send_data(-1)

            except Exception as e:
                print("[ERROR]Fail to accept connection", e)

    # Parse binary typed response
    def parse(self,data):
        if data == b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n':
            return -1

        return switch(data[3:4])

    def type_1(x):
        return self.parse_header(x)

    def type_2():
        return

    def type_3():

    def type_4():

    def type_5():

    def type_6():

    def type_7():

    def type_8():

    def type_9():

    # Parsed header save as dictionary type
    def parse_header(self,data):
        d = Decoder()
        decoded_headers = d.decode(data)

        dic_header = {}
        for str in decoded_headers:
            dic_header[str[0]] = str[1]

        return dic_header

    # Send data
    def send_data(self,mod):
        if mod == -1:
            self.conn.send(SERVER_PREFACE)



if __name__ == '__main__':
    setting = setting()
    conn = setting.RunServer()
    socket = OpenSocket(conn)
    conn = socket.run()
    server = http2(conn)
    server.run()
