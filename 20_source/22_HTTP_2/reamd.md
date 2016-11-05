# HTTP2 Sample


## Request
```
Method: GET
Protocol: HTTP/2.0
Host: http2.golang.org
RemoteAddr: 123.142.203.91:10079
RequestURI: "/reqinfo"
URL: &url.URL{Scheme:"", Opaque:"", User:(*url.Userinfo)(nil), Host:"", Path:"/reqinfo", RawPath:"", ForceQuery:false, RawQuery:"", Fragment:""}
Body.ContentLength: 0 (-1 means unknown)
Close: false (relevant for HTTP/1 only)
TLS: &tls.ConnectionState{Version:0x303, HandshakeComplete:true, DidResume:false, CipherSuite:0xc02f, NegotiatedProtocol:"h2", NegotiatedProtocolIsMutual:true, ServerName:"http2.golang.org", PeerCertificates:[]*x509.Certificate(nil), VerifiedChains:[][]*x509.Certificate(nil), SignedCertificateTimestamps:[][]uint8(nil), OCSPResponse:[]uint8(nil), TLSUnique:[]uint8{0xe0, 0x78, 0x38, 0x9d, 0xa2, 0xcc, 0x5b, 0xdf, 0x1f, 0x3, 0xe5, 0x82}}
```

## Response
### 302
<pre>
<code>
content-length:24
content-type:text/html; charset=utf-8
date:Fri, 04 Nov 2016 11:40:56 GMT
location:/
status:302
</code>
</pre>

### 200
<pre>
<code>
content-length:1708
content-type:text/html; charset=utf-8
date:Fri, 04 Nov 2016 11:44:04 GMT
status:200
</code>
</pre>

### 200 (files)
<pre>
<code>
accept-ranges:bytes
content-length:10921353
content-type:application/x-gzip
date:Fri, 04 Nov 2016 11:44:28 GMT
last-modified:Wed, 02 Nov 2016 13:21:41 GMT
status:200
</code>
</pre>
