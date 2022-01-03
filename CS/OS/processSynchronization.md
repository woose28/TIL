## 📌 프로세스 동기화(Process Synchronization)

### 💡 사전 지식
1. 협력적 프로세스
    - 다른 프로세스의 실행에 영향을 주거나, 다른 프로세스의 실행에 의해 영향을 받는 프로세스

2. 경쟁 상태(race condition)
    - 여러 프로세스가 같은 데이터에 접근하고, 접근 순서에 따라 결과가 달라지는 상황

3. 원자적 연산(atomic operation)
    - `원자성(atomic)`은 원자처럼 분리할 수 없는 또는 쪼갤 수 없는 성질을 의미한다.
        - 실제로는 원자보다 더 작은 입자가 존재한다고 한다.
        - `원자성`에 대한 예시는 [여기서](https://ko.wikipedia.org/wiki/원자성_(데이터베이스_시스템)) 확인 가능하다.
    - `원자적 연산`은 하나의 공유 변수에 동시에 하나의 스레드만 접근하는 것을 보장하는 연산
        - 이는 원자적 연산 수행 도중에 `문맥 교환(context swtiching)`이 발생하지 않는 것을 의미
        - `원자적 연산`에 대한 조금 더 자세한 설명은 [여기서](https://mygumi.tistory.com/111) 확인 가능하다.
    
<br>

### ✔️ 프로세스 동기화(Process Synchronization)란?
- 여러 프로세스들이 동시에 공유 데이터에 접근하는 상황에서, 일관된 결과를 유지하기 위해 실행 순서를 정해주는 메커니즘
- 즉, `경쟁 상태(race condition)`을 해결하기 위해 협럭 프로세스간의 동기화가 필요하다.

<br>

### ✔️ 임계 구역(Critical Section)이란?
- 프로세스의 코드 중 다른 프로세스와 공유하는 데이터에 접근하고 갱신하는 영역
- 예시
```c
do {
	entry section # 임계 구역의 진입을 요청하는 부분
	    critical section
	exit section # 임계 구역의 퇴출을 알리는 부분
	    remainder section
} while (1);
```

<br>

### ✔️ 임계 구역 문제를 해결하기 위한 조건
1. 상호 배제(Mutual Exclusion)
    - 하나의 프로세스가 임계 구역에 진입하여 실행된다면, 다른 프로세스들은 임계 구역의 코드를 실행할 수 없다.
2. 진행(Progress)
    - 임계 구역의 코드를 실행 중인 프로세스가 없고 하나의 프로세스가 임계 구역의 코드를 실행하려 한다면, 해당 프로세스가 임계 구역의 코드를 실행하는 것을 허용해야 한다.
3. 한정된 대기(Bounded Waiting)
    - 하나의 프로세스가 임계 구역으로 진입을 요청하고 진입이 허용될 때까지 다른 프로세스들이 임계 구역으로 들어가는 횟수에 한계가 있어야 한다.
    - 즉 P0가 임계 구역의 코드를 실행하려 요청한 상태에서, P1과 P2가 서로 임계 구역의 코드 실행권을 독점하고 있으면 안된다.

<br>

### ✔️ 임계 구역을 다루기 위한 커널을 방식
- 커널에서도 임계 구역 문제가 발생한다.
    - 서로 다른 프로세스가 동시에 `fork()` 시스템 콜을 실행하는 경우
        - 자식 프로세스의 pid 값을 결정하기 위해 두 프로세스가 `next_available_pid` 변수에 동시에 접근하게 된다.
- 임계 구역 문제를 다루기 위한 대표적인 방식
    - 선점형 커널
        - 프로세스가 커널 모드에서 수행되더라도, 선점될 수 있는 방식
        - 커널 모드의 각 자료 구조에 경쟁 조건이 발생하지 않도록 따로 처리를 해줘야한다.
    - 비선점형 커널
        - 하나의 프로세스가 커널 모드에서 수행중이라면, 해당 프로세스는 커널 모드에서 작업이 끝날 때까지 선점되지 않는 방식
        - 하나의 프로세스만 커널 모드에서 수행되는 사실을 보장할 수 있다

<br>

### ✔️ 피터슨 알고리즘(Peterson's algorithm)
- 임계 구역 문제를 해결하기 위한 알고리즘
- 문제점
    - `바쁜 대기(busy waiting)` 문제가 존재
    - 다중 스레드 상황에서 명령어 실행 순서에 따라 임계 영역에서 두 개의 프로세스가 동시에 실행되는 상황이 발생될 수 있음

<br>

### ✔️ 임계 구역 문제를 위한 해결책
1. 뮤텍스 락(Mutex Locks)
    - 내부적으로 `available` 변수를 갖는다.
    - `available` 변수가 `false`일 때만 임계 구역으로 진입이 가능하다.
    - `available` 변수를 변경할 수 있는 함수는 아래와 같다.
        - acquire() 함수
            - lock을 획득하는 함수이다.
            - 하나의 프로세스에서 lock을 획득하면 다른 프로세스는 lock이 반환될 때까지 기다려야한다.
                - 이때, `바쁜 대기(busy wait)` 문제가 발생한다. 
            - 함수 정의는 다음과 같다.
                ```c
                acquire() {
                    while(!available) // busy wait

                    available = false;
                }
                ```
        - relase() 함수
            - lock을 반환하는 함수이다.
            - 함수 정의는 다음과 같다.
                ```c
                release() {
                    available = true;
                }
                ```
    - `바쁜 대기(busy wait)` 문제가 있는 뮤텍스락을 스핀락(spinlock)이라고도 한다.

2. 세마포(Semaphore)
    - 추상 자료형이다.
        - 논리적으로 정의가 된 것이며, 실제 구현된 건 아니다.
    - 내부적으로 `정수 값(integer variable)`을 갖는다.
    - 이 `정수 값`은 공유 자원의 개수를 의미한다.
    - 공유 자원을 획득하기 위한 연산은 두 가지가 있다.
        - P 연산
            - 공유 자원을 획득하는 연산
            - 이용할 수 있는 자원이 있으며, P 연산을 요청한 프로세스가 자원을 점유한다.
        - V 연산
            - 공유 자원을 반환하는 연산
    
    - 세마포를 구현하는 방식
        - Busy-wait 방식
            - 사용할 수 있는 자원이 없으면 while문을 통해 계속 대기한다.
            - 대기하는 동안 CPU를 낭비하는 단점이 있다.
        - Block/Wakeup 방식
            - 세마포 내부적으로 큐가 존재하며
            - P 연산 호출 시 자원을 획득하지 못한 프로세스는 `sleep()` 시스템 콜을 호출하고 큐에서 대기하게된다.
                - 이떄 CPU 제어권은 다른 프로세스에게 이양된다.
            - S 연산을 호출하고 큐에서 대기하는 프로세스가 있다면 해당 프로세스를 큐에서 꺼내 `wakeup()` 시스템 콜을 호출한다.
            - Block/Wakeup 방식은 `문맥 교환(Context Switch)`에 의한 overhead가 발생할 수 있다.
            - Block/Wakeup 방식에서는 세마포를 다음고 같이 정의한다.
                ```c
                typedef struct {
                    int value;
                    struct process *list;
                } semaphore
                ```
            
    - `정수 값`에 따른 세마포 종류
        - 이진 세마포(Binary Semaphore)
            - `정수 값`으로 0과 1만 가지는 세마포
            - `뮤텍스 락`과 비슷하며 상호배제를 구현하기위해 주로 사용된다.

        - 카운팅 세마포(Counting Semaphore)
            - `정수 값`을 사용할 수 있는 자원의 개수로 초기화한다.
            - `정수 값`은 가용 자원의 수를 의미한다.
    
    - 세마포 사용 시 문제점
        - 경우에 따라 `Deadlock(교착 상태)`가 발생할 수 있다.

3. 모니터(Monitor)
    - 추상 자료형이다.
    - 모니터 내부에 정의된 공유 변수들은 모니터 내부에 정의된 함수에 의해서만 접근 가능하다.
    - 모니터는 내부적으로 `상호배제`가 구현되어 있다.
        - 모니터 내부에서 동시에 하나의 프로세스만 실행 가능하다.

    - 조건 변수(condition variable)
        - 조건 변수에는 두 가지 연산이 존재한다.
            - wait()
                - 자신의 큐에 현재 `wait()`를 호출한 프로세스를 대기 시킨다.
                - `wait()`을 호출한 프로세스는 다른 프로세스가 `signal()`을 호출할 때까지 `suspend` 상태가 된다.
            - signal()
                - 자신의 큐에서 대기하고 있는 프로세스를 깨운다.
                - 조건 변수에 대기하고 있는 프로세스를 다시 실행시킨다.
        
    - 모니터 구현 예시(생산자-소비자 문제)
        ```c
        monitor bounded_burffer {
            int buffer[N];
            condition full, empty
            /*
                condition variable은 값을 가지지않고, 자신의 큐에 프로세스를 매달아서 sleep 시키거나
                큐에서 프로세스를 깨우는 역할만 한다.
            */
            
            void produce(int x){
                if there is no empty buffer
                    empty.wait();
                add x to an empty buffer
                full.signal();
                /*
                    만약 full에서 잠들어 있는 프로세스가 없다면, 아무 일도 발생하지 않는다.
                */
            }


            void consume(int *x) {
                if there is not full buffer
                    full.wait();
                remove an item from buffer and store it to *x
                empty.signal()
                /*
                    만약 empty에 잠들어 있는 프로세스가 없다면, 아무 일도 발생하지 않는다.
                */
            }
        }
        ```
    
<br>

### ✔️ 동기화(Synchronization)와 관련된 고전적인 문제 예시
1. [생산자-소비자 문제(Producer–consumer problem 또는 Bounded-Buffer problem)](https://ko.wikipedia.org/wiki/생산자-소비자_문제)
2. [독자-저자 문제(Readers–writers problem)](https://ko.wikipedia.org/wiki/독자-저자_문제)
3. [식사하는 철학자들 문제(Dining philosophers problem)](https://ko.wikipedia.org/wiki/식사하는_철학자들_문제)

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Process Synchronization - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
- 운영체제 Ch.6 동기화 도구들 - Abraham Silberschatz 외 2인
- [원자성 (데이터베이스 시스템) - 위키백과](https://ko.wikipedia.org/wiki/원자성_(데이터베이스_시스템))
- [Atomic Operation이란? - 마이구미의 HelloWorld](https://mygumi.tistory.com/111)