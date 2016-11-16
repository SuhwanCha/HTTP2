import socket
import binascii
from threading import Thread
import _thread

_status_code_to_msg = {
    100: 'Continue',
    101: 'Switching Protocols',
    200: 'OK',
    403: 'Forbidden',
    404: 'NOT FOUND',
    500: 'Internal Server Error',
}

class run(Thread):
    def __init__(self,HOST,PORT):
        self.HOST = HOST;
        self.PORT = PORT;
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((self.HOST,self.PORT))
        self.connection.listen(5)

        print('Run server at '+HOST+':'+str(PORT))
        Thread.__init__(self)

    def check_status(self,file_name):
        if file_name == '/' :
            temp = './index.html'
        else :
            temp = '.'+str(file_name)

        try :
            f = open(temp, 'r', encoding='utf-8')
            status = 200
        except FileNotFoundError:
            status = 404
        except PermissionError:
            status = 403
        return status


    def create_status_line(self,status_code):
        return str("HTTP/1.1 " + str(status_code) +\
            _status_code_to_msg[status_code] + '\r\n')

    def create_header(self):
        return 'Server: python/3.5.2\r\n'\
                   'Content-Type: text/html; charset=\"utf-8\"\r\n\r\n'

    def create_data(self,file_name):
        if file_name == '/' :
            temp = './index.html'
        else :
            temp = '.'+str(file_name)
        f = open(temp, 'r', encoding='utf-8')
        return f.read()

    def parse_header(self,data):
        component = data.decode('utf-8').split('\r\n')
        try :
            headers = component[0].split(' ')
            method = headers[0]
            url = headers[1]
            http_version = headers[2].split('/')[1]
            self.print_info(method,url,http_version)
        except :
            print('ERROR!')
            url = '404'
        return url

    def print_info(self,method,url,http_version):
        print(method,url,'('+http_version+')')

    def run(self):
        # print("run thread")
        conn, addr = self.connection.accept()
        data = conn.recv(1024)
        url = self.parse_header(data)
        status = self.check_status(url)
        response = self.create_status_line(status)
        response += self.create_header()
        if(status == 200) :
            response += self.create_data(url)
        response = response.encode(encoding='UTF-8')
        conn.send(response)
        conn.close()
        _thread.start_new_thread(self.run())


if __name__ == '__main__':
    serve = run('127.0.0.1',8080)
    serve.start()
