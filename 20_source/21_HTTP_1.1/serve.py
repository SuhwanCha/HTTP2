import socket

HOST = '127.0.0.1'
PORT = 9999

_status_code_to_msg = {
    200: 'OK',
    404: 'NOT FOUND',
}

def create_status_line(status_code):
    return "HTTP/1.1" + str(status_code) + \
        _status_code_to_msg[status_code]

def serve():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((HOST,PORT))
    connection.listen(1)

    while True:
        conn, addr = connection.accept()
        data = conn.recv(1024)
        print(data)

        create_status_line()
        create_header()
        create_body()

        conn.sendall("HTTP/1.1 200 OK\r\n"\
        "Server: python/3.5.2\r\n"\
        "Content-Type: text/html; charset=\"utf-8\"\r\n\r\n"\
        "<html><head><title>HTTP 1.1</title></head><body><h1>Hello HTTP 1.1</h1></body></html>"
        .encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    serve()
