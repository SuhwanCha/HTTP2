# RFC7540(HTTP2) Structure - Header

## 샘플
<pre>
<code>
POST /resource HTTP/1.1          HEADERS
Host: example.org          ==>     - END_STREAM
Content-Type: image/jpeg           - END_HEADERS
Content-Length: 123                  :method = POST
                                     :path = /resource
{binary data}                        :scheme = https

                                 CONTINUATION
                                   + END_HEADERS
                                     content-type = image/jpeg
                                     host = example.org
                                     content-length = 123

                                 DATA
                                   + END_STREAM
                                 {binary data}
</code>
</pre>

<pre>
<code>
HTTP/1.1 100 Continue            HEADERS
Extension-Field: bar       ==>     - END_STREAM
                                   + END_HEADERS
                                     :status = 100
                                     extension-field = bar

HTTP/1.1 200 OK                  HEADERS
Content-Type: image/jpeg   ==>     - END_STREAM
Transfer-Encoding: chunked         + END_HEADERS
Trailer: Foo                         :status = 200
                                     content-length = 123
123                                  content-type = image/jpeg
{binary data}                        trailer = Foo
0
Foo: bar                         DATA
                                   - END_STREAM
                                 {binary data}

                                 HEADERS
                                   + END_STREAM
                                   + END_HEADERS
                                     foo = bar

</code>
</pre>

## 기초
  * key:value 인덱싱 지원
  * key는 모두 소문자로 사용해야함

## Cookie
만약 a=b; c=d 라는 쿠키가 있다고 하자. 
* HTTP 1.1
  * cookie: a=b; c=d;
  * 이 경우에 값 하나만 바뀌면 다시 다 받아와야함
* HTTP 2
  * cookie: a=b
  * cookie: c=d
  * **나눠서** 보냄
  * 이 경우에 SESSION같은 쿠키는 잘 안바뀌기 때문에 빠름

##Virtual Header
1. :satus
2. :authority
3. :scheme
4. :method
5. :path
* HTTP/1.1 200 OK 같은 부분이 없어지고 Virtual Header를 사용함. 샘플 참고
