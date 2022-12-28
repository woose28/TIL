
# 애플리케이션 계층

## 요약

- HTTP
    - Hyper Text를 전달하기 위해 TCP 통신을 이용하는 프로토콜이다. 대표적으로 브라우저에서 HTML 문서를 전달할 때 사용한다.
    - 연결 지향이며 무 상태성 특징을 가진다.
    - HTTP1.1부터는 Connection: keep-alive 헤더가 기본으로 설정돼 있다. 따라서 한 번 TCP 연결을 하면 여러 리소스를 요청할 수 있다.
    - HTTP가 무 상태성이라는 특징을 가지고 있어서 Cookie, Local Storage 등의 브라우저 저장소가 생겨났다.
- DNS
    1. DNS는 도메인 이름을 IP 주소로 변환하는 시스템이다. DNS Name 서버는 계층구조로 되어있다.
    2. IP주소를 알아내기 위해 브라우저 캐시 → OS 호스트 파일 → DNS 서버 순으로 조회한다.
    3. DNS 서버에서 조회할 때는 먼저 인터넷망의 Local DNS Name 서버를 우선 조회한다. 그 후 재귀적으로 Root DNS Name 서버부터 IP 조회를 한다.
    4. DNS 서버와의 통신은 기본으로 53번 포트를 이용하면 UDP 통신을 한다.
- Socket
    1. 애플리케이션 간의 통신을 하려는 interface이다.
    2. Socket에는 두 가지의 종류가 있다. SOCK_STREAM은 TCP 소켓을 의미하며, SOCKET_DGRAM은 UPD 소켓을 의미한다.

<br />

## 네트워크 용어

네트워크

- 서로 다른 컴퓨터에서 동작하는 프로세스 간에 데이터를 주고받는 것

소켓

- 다른 컴퓨터의 프로세스와 통신하기 위한 통로
- IP주소와 port 번호로 식별할 수 있다.

<br />

## 전송 프로토콜의 종류

### TCP

신뢰성 있는 전달 프로토콜이다.

- 연결 지향
- 혼잡 제어
- 흐름 제어

<br />

### UDP

비신뢰성 데이터 전달 프로토콜이다.

<br />

## HTTP

HyperText(링크가 있는 텍스트)를 전달하는 프로토콜

- HTTP는 기본적으로 TCP를 기반으로 동작한다.
    - 버전에 따라 다르다.
    - HTTP3.0의 경우 UDP 기반으로 동작한다.
- HTTP는 기본적으로 stateless(무상태성)이다.
    - localStorage, sesstionStorage 등의 브라우저 저장소가 필요한 이유도 이런 특성 때문이다.
- HTTP 버전에 따라 TCP 연결을 재활용할 수 있다.
    - non-persistent HTTP: 데이터를 전송할 때마다 TCP 연결을 새로 한다.
        - non-persistent HTTP의 응답 시간: 2RTT + transmission time
    - persistent HTTP: 한 번 TCP 연결을 하면 데이터를 필요한 데이터를 연속해서 주고받는다.
        - 해당 기능은 Connection 헤더 값을 통해 설정할 수 있다. 하지만, HTTP2.0과 3.0에서는 해당 헤더의 사용이 금지돼 있다.
        - HTTP1.1 버전부터는 `Connection: keep-alive` 이 기본으로 설정돼 있다.
        

<br />

💡RTT란?

> Time for a small packet to travel from client to server and back
> 

<br />

💡propagation delay란?

> 첫 패킷이 서버에 도착하고 마지막 패킷이 서버에 도착할 때까지 걸리는 시간 차
>

## Cache의 사용

Cache는 리소스를 더 빠르게 제공하기 위해서 사용한다. 

하지만 Cache는 원본 리소스에 대한 복사본을 사용하기 때문에 Cache와 원본 리소스를 일치시켜야 하는 추가 작업이 필요하다. 웹 브라우저에서는 이를 조건부 요청을 통해 이 문제를 해결한다. GET 요청 시 **If-Modified-Since** 헤더를 사용하면 조건부 요청을 보낼 수 있다. 만약 리소스가 해당 헤더 값에 지정된 시간 이후로 수정된 부분이 없다면 304 응답을 반환한다.

💡 프록시 서버에서 Cache 데이터의 일관성을 증가시키기 위해 TTL(Time to live)이 사용될 수 있다.

<br />

## DNS

DNS(Domain Name System)은 URL을 IP 주소로 변환하는 시스템이다. 이런 일을 해주는 서버를 Name 서버라고 한다.

하나의 Name 서버에서 URL을 IP를 변환하는 작업을 모두 수행하면 부하가 심할 것이다. 따라서 이러한 성능 부하를 방지하기 위해 Name 서버는 계층화가 되어있다.
- root domain server
- top-level domain(TLD) server
    - 최상위 도메인을 관리한다.
    - `com`, `edu` 등이 최상위 도메인에 속한다.
- second-level domain(=authoritative DNS server)
    - 특정 기관의 DNS 서버이다. 해당 서버에는 기관에서 운영 중인 host를 정의해둔다.
    - 도메인이 `www.naver.com`이라면  `naver`가 여기에 해당된다.

💡계층 구조로 root domain server는 top-level domain 서버에 대한 정보를 저장한다. 이처럼 각 레벨의 도메인은 그 하위 도메인에 대한 정보를 관리한다.

브라우저 주소창에 [www.naver.com](http://www.naver.com)를 입력하는 행위는 네이버의 www.naver.com 컴퓨터를 지칭하는 것이다. DNS 검색은 아래와 같은 과정으로 이뤄진다.

1. 브라우저 캐시에서 검색
2. 로컬의 host 파일을 참조
3. DNS 서버로 요청

💡 DNS 쿼리는  Local DNS Name 서버에서 우선 조회된다. Local DNS Name 서버에 없는 경우에 외부 DNS Server로 검색이 일어난다.

💡 Name 서버에서 재귀적으로 실제 IP주소를 찾는다.

💡 DNS 서버간 주고 받는 데이터의 크기는 매우 작다. 따라서 DNS 서버는 주로 53번 포트를 통해 UDP 통신을 한다.

<br />

### 참고 자료
[…하면 생기는 일 - DNS 검색](https://github.com/SantonyChoi/what-happens-when-KR#dns-%EA%B2%80%EC%83%89)


## DNS record

DNS Server는 RR format으로 데이터를 저장한다.

> RR format: (name, value, type, ttl)
> 

이중 type은 총 네 가지 값을 가진다.

- type=A
    - Address 레코드를 의미한다.
    - `type=A` 인 레코드에는 value에 실제 주소가 저장된다.
- type=NS
    - Name server 레코드를 의미한다.
    - DNS 서버에 대한 이름이 value에 저장된다.
    - value 값으로 type=A
- type=CNAME
- type=MX

<br />

## Socket

소켓은 어플리케이션 사이 또는 네트워크를 사이 간에 통신을 하기위한 interface이다.

소켓은 크게 두 가지의 종류가 있다.

- SOCK_STREAM
    - TCP 소켓이라고 한다.
- SOCK_DGRAM
    - UDP 소켓이라고 한다.

💡 TCP 통신의 connect()은 3-handsake을 통해 Socket간의 연결을 하는 과정인가?

<br />

## SMTP와 POP3

이메일과 관련된 프로토콜이다.

- SMTP
    - 이메일을 보낼 때 사용하는 프로토콜이다.
    - SMTP는 25번 포트를 사용한다.
- POP3
    - 이메일을 수신할 때 사용하는 프로토콜
    - POP3는 110번 포트를 사용한다.

💡메일 서버에는 사용자별로 메일을 보관하는 메일 박스가 있다. 사용자가 메일 박스에 보관된 메일 정보를 가져올 때 서버와 POP3 프로토콜로 통신한다.