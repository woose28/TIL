
# 애플리케이션 계층

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