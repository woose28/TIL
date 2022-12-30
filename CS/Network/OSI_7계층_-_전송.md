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

<br />

## TCP의 특징

- point-to-point
    - sender와 recevier의 소켓이 1 대 1 매칭된다.
- reliable, in-order byte stream
    - 메시지가 보낸 순서대로 출발하고 도착한다.
- piplelines
    - window size를 설정하고 혼잡 제어와 흐름 제어를 할 수 있다.
- full duplex data
    - 양 방향으로 데이터를 주고받을 수 있다. sender가 receiver가 될 수 있고, receiver가 sender도 될 수 있다.
- connection-oriented
- flow controlled
    - 데이터 전송 속도를 recevier가 처리할 수 있는 속도에 맞춰서 조절한다.

<br />

## TCP 세그먼트 구조

TCP의 헤더 필드는 다음과 같다.

- source port
    - 출발 포트 번호이다.
- dest port
    - 도착 포트 번호이다.
- sequence number
    - 각 세그먼트를 식별하기 위해  사용한다.
    - byte 단위로 정해진다. data의 처음 byte 번호가 현재 세그먼트의 sequence number가 된다.
- acknowledegement number
    - receiver가 sender에게 세그먼트가 잘 도착했는지 정보를 전달하기 위해 사용하는 필드이다. acknowledegement number 필드에는 다음에 받아야할 sequence number가 저장된다.
    - 만약 acknowledegement number에 100이 저장됐다면 100번 시퀀스부터 데이터를 전달받으면 된다는 의미이다.
- receive window
    - 데이터를 전송받는 측의 receive buffer의 여유 공간의 크기이다.
    - sender는 receive window의 크기 확인하면서 send buffer의 window 크기를 조절한다.
- data offset
    - 전체 세그먼트 중에서 데이터가 시작되는 위치를 기록하는 필드이다.
    - 헤더의 옵션 필드의 길이가 가변적이기 때문에 해당 필드가 필요하다.
- flgas
    - 9개의 비트 플래그들이 있다. 현재 세그먼트가 어떤 종류의 세그먼트인지 플래그를 통해 표현한다.
- checksum
    - 데이터를 송신하는 도중에 발생할 수 있는 에러를 검출하기 위해 사용되는 필드이다.
- options
    - TCP의 기능을 확장할 때 사용하는 필드이다.

<br />

### 참고자료

[TCP의 헤더에는 어떤 정보들이 담겨있는걸까? - Evans Library](https://evan-moon.github.io/2019/11/10/header-of-tcp/)

<br />

## TCP Round trip time

TCP는 RTT를 계산하고 조금 더 여유로운 시간으로 Timer로 지정한다. RTT는 세그먼트를 보낼 때마다 측정한다. 이 RTT를 sample RTT라고 한다.

세그먼트를 보낼 때마다 Sample RTT의 값은 다르다. 이는 세그먼트 마다 receiver로 전달되는 라우터 경로와 라우터의 큐 상태가 다르기 때문이다.

💡 하지만 재전송한 세그먼트는 Sample RTT로 측정하지 않는다.

```tsx
EstimatedRTT = (1 - a) * EstimatedRTT + a * SampleRTT

// a = 0.125

TimeoutInterval = EstimatedRTT + (약간의 여유 시간) // TimeoutInterval은 실제 Timer의 시간이다.
```

<br />

## TCP의 신뢰할 수 있는 데이터 전송(reliable data transfer)

한 쌍의 TCP 소켓이 연결되면 각 소켓에는 send buffer와 receive buffer가 생성된다.

- send buffer
    - 전송할 세그먼트가 대기하는 버퍼이다.
    - 재전송하는 경우를 대비하여 세그먼트를 버퍼에 저장한다.
    
- receive buffer
    - 전송받은 세그먼트가 들어오는 버퍼이다.
    - in order delivery를 하기위해 버퍼이다. 세그먼트의 순서에 맞춰서 애플리케이션 계층에 제공하기 위해서 전송받은 세그먼트를 임시 저장한다.
    - 애플리케이션에서 receive call을 하면 receive buffer에 세그먼트가 애플리케이션으로 전달된다. 하지만 만약 세그먼트 유실이 발생했다면 call이 block된 후 세그먼트를 재전송 받으면 애플리케이션 계층으로 전달한다.

💡send buffer는 반대편의 receive buffer와 연결된다. 반대로 receive buffer는 반대 편의 send buffer와 연결된다.

TCP의 신뢰할 수 있는 데이터 전송을 위해 알아야할 용어는 다음과 같다.

1. window
    - TCP의 sender buffer에서 한 번에 전송할 수 있는 세그먼트의 범위이다. window size는 한 번에 전송할 수 있는 세그먼트들의 크기를 의미한다.
    - window size는 수신 측의 receive buffer의 receive window(receive buffer 여유 공간 크기)에 따라 조절된다.(이것이 흐름 제어이다.)
    
2. send base
    - window의 첫번째 세그먼트를 가리킨다. 세그먼트의 유실됐을 때 send base가 가리키는 세그먼트를 재전송(retransmit)한다.
    - 방금 전송한 세그먼트가 잘 전송됐다면 window를 다음에 전송할 sequenec number로 이동시킨다.(=send base를 응답으로 받은 acknowledegement number만큼 이동한다.)

1. receive window
    - 수신 측 receive buffer의 여유 공간이다.

💡 자세한 통신 과정을 복습하고 싶다면 [해당 강의](http://www.kocw.net/home/search/kemView.do?kemId=1312397&ar=relateCourse)의 28분부터 다시 듣기!

💡TCP 소켓은 운영체제 단에 구현돼 있다.

💡 실제로 TCP 통신는 양방향 통신이기 때문에 하나의 세그먼트로 데이터 전송과 피드백(ACK)를 함께 한다. 세그먼트 헤더 필드에 sequence number와 acknowledegement number 필드가 각각 존재하는 이유도 이 때문이다.

💡실제 TCP에서 동일한 acknowledegement number 세그먼트를 네 번 이상 응답으로 받으면 timeout이 되지 않아도 재전송을 한다. 즉 timeout이 지나지 않아도 유실됐다는 정황을 통해 재전송을 한다. 이를 TCP Fast Transmit이라고 한다.

<br />

## TCP의 흐름 제어(flow control)

TCP에서 세그먼트를 보내는 속도는 receiver의 receive buffer의 남아있는 빈 공간의 크기를 고려해서 결정해야 한다. receiver의 receive buffer의 남은 크기는 세그먼트 헤더의 receive window 필드 값으로 전송한다.

sender의 send buffer는 receive window의 값에 따라 한 번에 보낼 수 있는 세그먼트 크기(window size)를 조절한다.

<br />

### 흐름 제어의 코너 케이스

만약 receive window의 크기가 0이라면 sender는 세그먼트를 전송하지 않는다. 더불어 receiver에서 새로 전송할 세그먼트가 없다면 두 소켓 사이에 아무런 세그먼트가 오가지 않는다.

이런 상황을 해결하기 위해 만약 receive window가 0으로 응답받으면 sender는 크기가 작은 데이터를 전송하여 receiver의 receive buffer 크기를 파악한다.

<br />

## TCP 통신을 더 효율적으로 하려는 노력

<br />

### 세그먼트 크기를 결정하는 기준

가장 단순한 방법은 애플리케이션에서 전달받은 데이터를 하나의 세그먼트로 만들어서 보내는 것이다.

하지만 만약 애플리케이션 계층에서 데이터를 조금씩 보내고 이를 하나씩 세그먼트로 전송한다면 데이터보다 헤더가 더 큰 상황이 발생한다. 이는 낭비이다.

또한 통신 횟수를 감소시키는 관점에서 세그먼트의 크기는 크게 하는 것이 이상적이다.

**Nagle’s Algorithm**

1. 처음에는 데이터를 그대로 전송한다.
2. 처음 데이터를 전송한 후 다음 상황이 발생할 때까지 데이터를 축적한다.
    - ACK가 도착한 상황
    - maximum segment size(보통 1,500byte)까지 데이터가 축적된 상황
3. 2번 상황이 발생하면 전송하고 2번 과정을 반복한다.

이 알고리즘을 따르면 아래의 효과를 얻을 수 있다.

- 애플리케이션의 데이터 전달 속도 > 네트워크 속도
    - 세그먼트의 크기가 커진다.
- 애플리케이션의 데이터 전달 속도 < 네트워크 속도
    - 세그먼트의 크기가 작아진다.(네트워크 상황이 좋기 때문에 세그먼트의 오버헤드가 커도 무방하다.)

<br />

### Receiver의 receive window 크기를 결정하는 방법

만약 receive window의 크기가 매우 작다면 전달받은 세그먼트의 크기가 매우 작아지기 때문에 통신상 비효율이 발생한다.

그 때문에 최소값을 정하고 이보다 receive window가 작아지면 세그먼트 헤더의 receive header 필드에 0 값을 담아 전달한다.

<br />

### Delay ACK

네트워크 요청을 횟수를 줄이기 위해 세그먼트가 도착하면 바로 ACK를 보내지 않고 약간의 시간 동안 대기한 후 최근에 도착한 sequence number에 해당하는 ACK를 한 번만 보낸다.

<br />

## 연결 관리(Connection Management)

TCP는 3-way-handshake 방식으로 각 소켓을 연결하며, 4-way-handshake 과정을 거치면서 소켓 연결이 해제된다.

<br />

### 3-way-handshake

1. TCP 세그먼트의 flag 필드의 SYN bit가 1로 설정하여 세그먼트를 전송한다. 이를 SYN 메시지라고 한다.
    - SYN 메시지는 데이터 부분은 없고 헤더만 전달된다.
2. receiver는 flag 필드의 SYN bit와 ACK bit를 1로 설정하고 응답 세그먼트를 전송한다. 이를 SYNACK 메시지라고 한다.
    - TCP SYNACK 메시지는 데이터 부분은 없고 헤더만 전달된다.
3. SYNACK 메시지를 받은 sender는 flag 필드의 ACK bit를 1로 설정하고 segment를 보내면서 통신이 시작된다. 해당 메시지는 ACK 메시지이다.
    - ACK 메시지부터는 세그먼트에 전달할 데이터를 함께 전달한다.

<br />

### 4-way-handshake

1. TCP 세그먼트의 flag 필드의 FIN bit가 1로 설정하여 세그먼트를 전송한다.
2. receiver는 TCP 세그먼트의 flag 필드의 ACK bit가 1로 설정하여 세그먼트를 전송한다.
3. sender는 reciever가 FIN 메시지를 보낼 때까지 대기한다.
4. receiver가 FIN 메시지를 전송한다. sender는 자원을 회수하지 않고 잠시 대기하며 ACK 메시지를 전송한다.
    - ACK 메시지가 유실됐을 때 sender가 다시 ACK 메시지를 전달해야하기 때문에 sender는 바로 자원을 회수하지 않는다.
5. sender가 ACK 메시지를 전송한다. receiver는 ACK 메시지를 받으면 자원을 회수한다.
6. 대기 시간이 끝나면 sender 역시 자원을 회수한다.

🤔 왜 TCP 연결을 종료하는 과정은 4-way-handshake일까? → Client와 Server 모두 send와 receive 역할을 할 수 있기 때문이라고 생각한다.

<br />

## TCP의 혼잡 제어(Congestion Control)

혼잡 제어는 네트워크 상황에 따라 세그먼트를 보내는 속도를 결정하는 것을 의미한다.

<br />

### 혼잡 제어가 필요한 이유

모든 TCP sender가 네트워크 상태를 고려하지 않고 세그먼트를 전송한다면 네트워크는 과부하 상태가 된다.

이런 상황이 오면 sender가 보낸 세그먼트는 receiver에게 전달되지 않는 현상이 발생할 수 있다. 따라서 원활한 통신을 위해서 네트워크 상황을 고려해서 세그먼트 전송 속도를 결정하는 혼잡 제어가 필요하다.

<br />

### 혼잡 제어 원리

혼잡 제어를 위해 congestion window size(cwnd)가 있다. 이는 send buffer의 window size를 결정짓는 요소 중 하나이다.

💡window size는 cwnd와 rwnd 중 작은 값으로 설정된다.

💡 maximum segemnt size는 보통 1,500byte이다.

cwnd를 증가시키는 방법은 아래와 같다.

- 특정 임계점 이하일 때는 세그먼트의 ACK가 정상적으로 도착하면 cwnd를 지수적으로 증가시킨다.
- 특정 임계점 이상일 때는 세그먼트의 ACK가 정상적으로 도착하면 cwnd를 1MSS(세그먼트 하나)만큼 증가시킨다. 즉 선형적으로 증가시킨다.

패킷이 유실됐을 때 cwnd를 감소시킨다. 패킷이 유실되는 상황은 timeout과 triple duplicate ACK으로 나뉜다. TCP 버전별로 패킷이 유실되는 상황에 따라 cwnd를 감소시키는 방법이 다르다.

- TCP 최초 버전(Tahoe)에서는 timeout 상황과 triple duplicate ACK 상황 모두 cwnd를 1MSS로 설정한다.
    - 또한 특정 임계점(sstresh)를 현재 cwnd의 반으로 설정한다.
- TCP 두 번째 버전(Reno)에서는 각 상황별로 cwnd를 감소시키는 방법이 다르다.
    - timeout이 발생하면 임계점을 현재 cwnd의 반으로 설정한다. 또한 cwnd를 1MSS로 설정한다.
    - triple duplicate ACK가 발생하면 임계점을 현재 cwnd의 반으로 설정한다. 또한 cwnd 또한 반으로 감소시킨다.

<br />

## TCP 전송 속도(throughtput)

TCP의 전송 속도는 네크워크 상황에 따라 조절된다. 때문에 파일을 웹에서 다운받을 때 속도가 실시간으로 변한다.

avg TCP throught = 3/4 * W / RTT

💡 UDP의 전송 속도는 애플리케이션이 결정한다.

💡 TCP의 혼잡 제어가 없으면 네트워크 과부화에 의해서 sender 패킷을 전송하지만 receiver는 패킷을 받지 못할 것이다.

💡 TCP의 대표적인 기능은 `신뢰 가능한 데이터 전송`, `흐름 제어`, `혼잡 제어`이다.

<br />

## TCP Fairness

TCP는 혼잡 제어에 의해서 여러 사용자의 congestion size는 공평하게 조절된다.

예를들면 badnwith가 R이고 두 명의 사용자게 데이터를 전송하면 각 사용자는 R/2 씩 데이터를 전송하게 된다.