# HTTP2Server

```
FROM RFC7540 offical
                         +--------+
                 send PP |        | recv PP
                ,--------|  idle  |--------.
               /         |        |         \
              v          +--------+          v
       +----------+          |           +----------+
       |          |          | send H /  |          |
,------| reserved |          | recv H    | reserved |------.
|      | (local)  |          |           | (remote) |      |
|      +----------+          v           +----------+      |
|          |             +--------+             |          |
|          |     recv ES |        | send ES     |          |
|   send H |     ,-------|  open  |-------.     | recv H   |
|          |    /        |        |        \    |          |
|          v   v         +--------+         v   v          |
|      +----------+          |           +----------+      |
|      |   half   |          |           |   half   |      |
|      |  closed  |          | send R /  |  closed  |      |
|      | (remote) |          | recv R    | (local)  |      |
|      +----------+          |           +----------+      |
|           |                |                 |           |
|           | send ES /      |       recv ES / |           |
|           | send R /       v        send R / |           |
|           | recv R     +--------+   recv R   |           |
| send R /  `----------->|        |<---------->'  send R / |
| recv R                 | closed |               recv R   |
`----------------------->|        |<-----------------------'
                         +--------+

send:   endpoint sends this frame
recv:   endpoint receives this frame

H:  HEADERS frame (with implied CONTINUATIONs)
PP: PUSH_PROMISE frame (with implied CONTINUATIONs)
ES: END_STREAM flag
R:  RST_STREAM frame
```

## About this project
![HTTP](http://httpwg.org/asset/http.svg)  
![한국디지털미디어고등학교](http://dimigo.hs.kr/layouts/dimigo_v2/images/static.logo.png)  
* License : [MIT](LICENSE)


## Reference
* [Wiki](https://en.wikipedia.org/wiki/HTTP/2)
* [Offical Page](https://http2.github.io/)
* [RFC7540](https://tools.ietf.org/html/rfc7540)
* [Luavis' Dev story](https://b.luavis.kr/http2/)
