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

<br />

## IPv4와 IPv6

IPv4 패킷의 source ip 필드와 dest ip 필드는 32bit이다. 즉 2^32개의 host를 지원할 수 있다.

IPv6 패킷의 source ip 필드와 dest ip 필드는 128bit이다. 즉 2^128개의 host를 지원할 수 있다.

96년도에 IPv4의 주소 부족 문제를 우려해서 IPv6를 도입했다. 하지만, 여전히 IPv4를 사용하고 있다.

그 이유는 대부분의 라우터는 IPv4를 지원하고 있고 라우터 마다 소유주가 다르기 때문에 모든 기기를 한 번에 교체하기는 어렵다.

💡IPv4를 지원하는 라우터와 IPv6를 지원하는 라우터가 하기 위해서는 서로가 이해할 수 있는 형식으로 패킷을 변경하는 Tunneling 작업을 해야 한다.

하지만 주소 부족 문제는 현실화가 되는데, 이 문제를 해결하기 위해 Network Address Translation(NAT)가 도입됐다.

<br />

### NAT

- gateway 내부적으로는 유니크한 주소 체계를 사용하고, LAN 외부로 요청을 보낼때 gateway에서 source ip주소와 port 번호를 변환해주는 방식이다.

💡gateway ip 주소는 global로 유니크하다.

- gateway는 내부적으로 NAT translation table을 갖고 있는다.
- NAT translation table에는 WAN side address 칼럼과 LAN side address 칼럼을 갖고 있다.
    - LAN side address에는 요청에 대한 source ip와 port 번호가 저장된다.
    - WAN side address에는 gateway의 ip 주소와 고유한 port 번호가 저장된다. port 번호를 통해 실제로 발생한 요청을 식별한다.
        - 즉, LAN 내부에서 발생한 요청의 source ip와 port를 WAN size address에 저장된 값으로 변경하고, 응답받을 때는 NAT translation table을 참고하여 dest ip와 port를 LAN side address로 변환한다.

💡기본적으로 NAT translation table에는 LAN에서 WAN으로 나가는 요청에 대한 변환 값만 저장한다. 때문에 클라이언트 측에서 NAT를 이용하는 것은 문제없다. 하지만 외부에서 먼저 요청을 받는 서버를 운영할 때는 적합하지 않다.

💡NAT 방식은 gateway에서 패킷과 세그먼트의 헤더를 필드 값을 수정한다는 미심쩍은 부분이 있다.

<br />

## DHCP(Dynamic Host Configuration Protocol)

DHCP는 각 디바이스에 동적으로 IP주소를 배정하는 방식이다.

💡각 디바이스가 항상 인터넷 통신을 하지 않기 때문에 고정으로 ip 주소를 할당하는 것은 비효율적이다.

<br />

### DHCP 서버

- IP 주소를 배정해주는 서버이다.
- DHCP 서버 port 번호는 68번이다.

<br />

### DHCP 클라이언트

- DHCP 클라이언트는 IP 주소를 배정받는 기기이다. 디바이스의 IP주소를 배정받는 프로세스에 해당하는 포트 번호는 67번 포트이다.
- 클라이언트는 브로드캐스트(255.255.255.255:68) 요청을 보내서 DHCP 서버로부터 IP 주소를 배정받는다.

💡DHCP는 애플리케이션 계층 프로토콜이다.

💡DHCP는 UDP를 사용한다.

<br />

### IP주소를 전달하는 과정 DHCP

- DHCP discover
- DHCP offer
- DHCP request
- DHCP ACK

💡만약 동시에 두 개의 DHCP 클라이언트가 동시에 DHCP discover를 보낸다면? 어떻게 IP를 배정할까?

→ DHCP discover 요청을 보낼 때 transaction ID를 함께 보낸다. DHCP 서버는 DHCP offer를 보낼 때 transaction ID를 참고하여 각각의 요청에 대해 IP 주소를 배정한다.

💡DHCP 서버는 IP 주소뿐만 아니라 서브넷 마스크, gateway IP 주소, DNS 서버 IP 주소를 모두 전달한다.

<br />

## IP 단편화와 재조립(fragmentation와 reassembly)

MTU는 라우터의 링크에서 최대로 전송할 수 있는 패킷의 크기이다.

만약 링크의 MTU보다 더 큰 크기의 패킷을 보내려면 패킷을 단편화(fragmentation)해야 한다.

단편화된 패킷은 도착지에서 다시 재조립(reassembly)돼야 한다.

이 기능을 위해 사용되는 헤더 필드는 fragflag와 offset이 있다.

- fragflag
    - 현재 해당 패킷이 마지막 조각(fragment)인지 표현하는 헤더 필드이다.
    - fragflag가 0이면 마지막 조각이라는 의미이며, fragflag가 1이면 또 다른 조각이 존재한다는 의미이다.
- offset
    - 시작 데이터로부터 현재 조각에 저장된 데이터의 offset
    - 헤더의 크기를 줄이기 위해 실제 offset을 8로 나눈 값이 저장된다. 이로인해 3bit를 절감하는 효과를 얻을 수 있다.

<br />

## ICMP(Interet Control Message Protocol)

네트워크상에서 문제가 발생했을 때, 문제를 souce에게 알려주기 위해 사용되는 프로토콜이다.

예를 들어 IP 패킷의 TTL 필드가 0이 돼서 패킷의 lifetime이 종료됐을 때, ICMP로 source에 해당 정보를 알려준다.

<br />

## 라우팅 알고리즘

라우터의 포워딩 테잉블을 채워 넣는 작업을 라우팅이라고 한다.

라우팅 알고리즘을 통해 목적지까지 최댄 경로를 계산하여 포워딩 테이블을 채운다.

<br />

### link state 알고리즘

라우터 간의 모든 연결 정보를 알고 있을 때 사용하는 알고리즘이다. 이를 위해 모든 라우터가 자신의 연결 정보를 브로드캐스트를 통해 다른 라우터에 공유해야한다.

대표적인 link state 알고리즘은 다익스트라 알고리즘이 있다.

💡같은 연결 정보(graph 정보)에 대하여 각 라우터의 포워딩 테이블 결과는 다르다. 하지만 계산하는  방법은 동일하다.

💡인터넷에 대해서 모든 라우터의 연결 정보를 아는 것은 현실적으로 어렵다. 하지만 하나의 네트워크(같은 소유주의 라우터 모임)에 한하여 연결 정보를 아는 것은 가능하다. 따라서 하나의 네트워크 한해서 link state 알고리즘을 사용할 수 있다.
