## 네트워크 용어

- 인터넷
    - IP 프로토콜을 사용하는 디바이스들의 연결이다.
- 패킷
    - 네트워크 계층의 전송 단위이다.

<br />

## 세그먼트

전송 계층의 데이터 전송 단위는 세그먼트이다.

세그먼트의 구조는 크게 header와 data로 나뉜다.

- header
    - 출발지 포트(source port) 번호, 도착지 포트(dest port) 번호 등 부가 정보가 담겨 있다.
- data
    - 애플리케이션 계층에서 전달받은 데이터가 저장되는 부분이다.

💡sender의 전송 계층에서는 애플리케이션 계층에서 전달된 데이터를 세그먼트 단위로 나눈다. 반면, receiver의 전송 계층에서는 네트워크 계층에서 도착한 세그먼트의 데이터를 조합해서 애플리케이션 계층으로 전달한다.

<br />

## 멀티 플렉싱과 디멀티플렉싱(Multiplexing/demultiplexing)

멀티 플렉싱/디멀티플렉싱은 TCP와 UDP 모두 제공하는 기능이다.

- 멀티 플렉싱(=다중화)
    - sender가 소켓으로 부터 들어온 data에 전송 계층 헤더를 붙여서 네트워크 계층으로 전달하는 과정
- 디멀티 플렉싱(=역다중화)
    - reciver의 전송 계층에서 세그 먼트의 헤더 필드 정보를 이용해서 data를 목적지인 소켓에 전달하는 과정
    

<br />

### UDP의 멀티 플렉싱(=connectionless demultiplexing)

목적지 ip 주소와 port 번호 정보만을 이용해서 소켓에 데이터를 전달한다.

즉, 목적지의 ip 주소와 port 번호가 동일하면 동일한 소켓으로 데이터가 전달된다.

<br />

### TCP의 멀티 플렉싱(=connection-oriented demultiplexing)

TCP 프로토콜은 연결지향 프로토콜이다. 때문에 sender의 소켓과 receiver의 소켓이 연결돼 있어야 한다.

TCP의 멀티 플렉싱에서 소켓을 식별할 때 다음과 같은 네 가지 정보를 활용한다.

- source ip
- source port
- destination ip
- destination port

<br />

### 참고 자료

[네트워크: Transport layer 정리 - seungjuitmemo](https://seungjuitmemo.tistory.com/83)

<br />

## UDP 세그먼트

UDP 세그먼트 헤더의 필드는 총 네 가지가 있다.

1. source port(16bit)
    - 멀티 플렉싱/디멀티 플렉싱을 제공하기 위해 필요하다.
2. dest port(16bit)
    - 멀티 플렉싱/디멀티 플렉싱을 제공하기 위해 필요하다.
3. length
    - UDP 세그먼트의 길이
4. checksum(16bit)
    - 에러 여부를 판단하기 위해 사용하는 헤더 필드
    - 전송 중간에 세그먼트가 유실이 됐을 때는 확인하지 못하지만, 세그먼트의 에러 여부는 확인할 수 있다.
    - 비트 단위 연산을 통해 에러 여부를 판단한다. 자세한 내용은 [여기](https://limjunho.github.io/2021/06/05/UDP-cksum.html)를 참고하자.

💡UDP는 주로 효율성(속도)가 중요한 데이터를 전송할 때 사용한다. 예를들어 동영상 데이터를 전송할 때 UDP를 사용한다.

<br />

## RDT: 연습용 신뢰 기반 프로토콜

RDT는 신뢰성 있는 데이터 전송 프로토콜이다. RDT는 신뢰성 있는 데이터 전송을 위해 데이터 에러와 데이터 손실 문제를 해결해야 한다.

<br />

### RDT 프로토콜 가정

- sender에서 데이터를 전송하고 receiver에게 응답받을 때까지 다음 데이터를 전송하지 않는다.
- 전송 계층 하위 계층(네트워크 계층, 물리 계층 등)은 unreliable channel이면 해당 계층에서는 메시지 에러(message error)와 메시지 손실(message loss)가 발생할 수 있다.

<br />

### RDT 1.0

- 하위 계층이 reliable한 상태이다. 따라서 메시지 에러와 손실이 발생하지 않는다.
- 따라서 sender는 특별한 기능(헤더) 없이 그대로 데이터를 receiver에게 전달하면 된다.

<br />

### RDT 2.0

- 하위 계층에서 메시지 에러가 발생한다.(손실은 발생하지 않는다.)
- 이 문제를 해결하기 위해 필요한 조치와 방안은 다음과 같다.
    - 에러 감지
        - 이는 checksum bit로 가능하다.
    - 피드백
        - recevier가 전달받은 데이터에 에러가 없다면 ACKs(Acknowledgements) 응답을 sender에게 보낸다.
        - receiver가 전달받은 데이터에 에러가 있다면 NAKs(Negative acknowledgements) 응답을 sender에게 보낸다.
    - 재전송
        - sender는 receiver로부터 NAKs 응답을 받으면 해당 메시지를 재전송한다.

<br />

### RDT 2.1

- RDT 2.1 버전에서 재전송 기능이 생겼기 때문에 recevier는 해당 데이터가 처음 전송됐는지 또는 재전송 됐는지 판단할 데이터가 필요하다. 이를 위해 sequence nubmer가 필요하다.
- receiver는 재전송받은 패킷을 처리하진 않는다. 하지만 sender에게 피드백 응답은 보낸다.

<br />

### RDT 2.2

- NAK 피드백 대신 ACK 피드백에 sequence number를 함께 보내는 방식이다.
- receiver는 ACK 피드백에 최근에 도착한 정확한 응답에 대한 sequence number를 함께 보낸다. 만약, sender가 받은 ACK 응답의 sequence nubmer가 이전 ACK의 sequence number와 동일하다면 최근 메시지에 에러가 발생한 것이다. 따라서 이런 경우 최근 메시지를 재전송한다.

<br />

### RDT 3.0

- underlying channel이 error와 loss 둘 다 발생할 수 있다.
- sender 입장에서는 메시지의 유실과 피드백의 유실은 동일하다.timer를 설정해서 일정 시간 동안 응답이 도착하지 않다면(loss가 발생했다면) 데이터를 전송한다.
    - 적절한 timer 설정 시간은 상황에 따라 다르다.

<br />

### RDT 정리

RDT는 데이터 에러와 손실 문제를 처리하기 위해 각각 아래와 같은 방안을 사용한다.

- 데이터 에러
    - checksum
    - feedback
    - retransimission
    - sequence number
- 데이터 손실
    - timeout

실세계의 신뢰 기반 프로토콜은 더 복잡하지만, RDT와 원리가 유사하다. 즉, TCP도 동일한 원리로 신뢰 기반 통신이 구현됐다.
