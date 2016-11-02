# HTTP1

## sample request
<code>
'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36\r\nAccept:   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch, br\r\nAccept-Language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4\r\n\r\n'
b'GET /favicon.ico HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36\r\nAccept: */*\r\nReferer: http://localhost:8080/\r\nAccept-Encoding: gzip, deflate, sdch, br\r\nAccept-Language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4\r\n\r\n'
</code>
