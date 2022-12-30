## 패킷

- 네트워크 계층의 전송 단위이다.

<br />

## 라우터의 기능

1. 포워딩(forwarding)
    - 라우터로 들어온 패킷의 목적지를 확인한 후, fowarding table를 참조해서 알맞은 서브넷으로 패킷을 전달하는 작업이다.
2. 라우팅(routing)
    - fowarding table에 서브넷 정보를 채워 넣는 작업이다.

인터넷에 있는 라우터는 best effort이다. 이는 패킷을 포워딩해 주지만 패킷의 지연과 유실에 대해 처리는 해주지 않는다는 것을 의미한다.

💡Router는 네트워크 계층까지 구현돼있다. 전송 계층과 애플리케이션 계층은 구현돼 있지 않다.

💡라우터는 패킷의 지연과 유실에 대한 별도의 작업은 해주지 않는다. 이런 라우터의 특징을 best effort라고 한다.

<br />

## 포워딩 테이블

포워딩 테이블은 Destination Address Ragne와 Link interface 두 가지 컬럼이 존재한다.

1. Destination Address Ragne
    - 도착지 주소 범위이다. 패킷의 도착지 주소를 확인한 후 Destination Address Ragne 열을 참고하여 가장 많이 일치하는 Link interface로 패킷을 전달한다.
2. Link interface
    - 현재 라우터에서 다른 라우터로 연결된 interface이다.

💡 두 가지 이사의 Range에 매칭이되면 가장 길게 매칭된 interface를 선택한다.

## IP 프로토콜

현재 인터넷은 IP 프로토콜을 사용한다. IP 프로토콜의 data 부분에는 전송 계층에서 전달받은세그먼트가 저장된다.

IP 패킷의 대표적인 헤더 필드는 아래와 같다.

- source ip 주소
    - 출발지의 ip 주소이다.
- destination ip 주소
    - 도착지의 ip 주소이다.
- time to live
    - 라우터에서 포워딩 될 때마다 해당 헤더 필드 값을 1씩 감소시킨다.
    - 이는 패킷의 수명을 제한하는 용도로 사용된다.
- upper layer protocol
    - data의 종류가 어떤 프로토콜인지 명시한다.

💡IP 패킷과 TCP 세그먼트 헤더의 크기는 20byte이다.

<br />

## IP 주소 체계

- IP주소의 크기는 32bit이다.
- IP주소는 network interface를 가리킨다.
- 보통 IP 주소의 앞의 24bit는 네트워크(Network) 부분(네트워크 id = prefix id = subnet)이며 뒷부분 8bit는 호스트(Host) 부분(호스트 id)이다. 하지만 이는 고정 값이 아니며 실제로는 서브넷 마스크를 이용해서 네트워크 id와 호스트 id를 구분한다.

💡IP 주소의 앞의 24bit는 네트워크(Network) 부분(네트워크 id = prefix id = subnet)이며 뒷 부분 8bit는 호스트(Host) 부분(호스트 id)이다.

💡같은 네트워크에 속한 장치들은 네트워크 부분이 동일하다.

💡라우터의 forwarding table의 크기를 최적화하기 위해 IP 주소를 계층화 해야한다.

<br />

### 서브넷 마스크(subnet mask)

- 실제 IP 주소에서 네트워크 id 부분과 host id 부분을 구별하기 위해 사용되는 정보이다.
- 서브넷 마스크의 1로 지정된 bit까지 IP 주소에서 네트워크 id 부분으로 해석된다. 이를 제외한 ip 주소는 host id로 해석된다.
- 기관마다 필요한 호스트 id의 수가 다르기 때문에 네트워크 id의 길이는 가변적이다. 현대에는 기관의 규모에 맞게 prefix 크기를 유연하게 배정한다.

서브넷 마스크의 예시는 다음과 같다.

> 11111111/11111110/0000000/00000000
> 

만약 서브넷 마스크가 위와 같다면 해당 기관은 2^17 개의 host를 가질 수 있다.

💡라우터의 forwarding table은 prefix id로 다음 도착지를 구분한다.

<br />

## 서브넷(Subnet)

- 같은 네트워크 id를 가진 interface의 집합이다.
- 같은 Subnet에 있는 interface 간의 통신은 라우터를 거치지 않고 통신할 수 있다.

💡라우터는 여러 개의 서브넷에 속해있는 장비이다. 즉 여러 서브넷을 연결해주는 장치라고 생각할 수 있다.
