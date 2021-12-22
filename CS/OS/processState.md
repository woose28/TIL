## 📌 프로세스 상태(Process State)

<br>

### 💡 사전 지식
1. 프로세스란?
    - 현재 실행 중인 프로그램

<br>

### 프로세스 상태
- New
    - 프로세스가 생성중인 상태
    - admitted
        - 상태 변화: `New` -> `Ready`
        - os `kernel`의 process management에 새로 생성된 process를 등록시키는 과정

- Ready
    - CPU를 부여 받으면 바로 명령문을 실행 가능한 상태
    - dispatch
        - 상태 변화: `Ready` -> `Running`

- Running
    - CPU를 사용하고 있는 상태
    - 만약 시스템에 CPU가 하나이며, `single core`라면 하나의 process만 CPU를 사용 가능
    - interrupt
        - 상태 변화: `Running` -> `Ready`
        - CPU를 사용중 interrupt를 받아 CPU 제어권을 잃는 과정
        - 주로 주어진 `time slice`를 모두 소진했을 때 발생한다.
    
- Blocked(Waiting)
    - CPU를 사용하는 중 I/O 작업이 필요하게 되면, CPU 낭비를 최소화하기 위해 `kernel`은 CPU 제어권을 다른 프로세스에게 넘기게된다.
    - 이때 I/O 작업이 필요한 프로세스는 `Blocked` 상태가 되고 I/O 작업을 기다린다.
    - wakeup
        - 상태 변화: `Blocked` -> `Ready`
        - I/O 작업과 같은 이벤트가 끝나게되면 해당 프로세스는 CPU 제어권을 부여받기 위해 `Ready`상태로 전환된다.

- Suspended(Stopped)
    - 외부 요청에 의해서 프로세스에 부여된 메모리를 빼앗긴 상태
        - 외부 요청
            - 사용자가 의도적으로 프로그램을 정지 시키는 경우
            - 메모리에 올라온 프로세스의 수가 너무 많아, `중기 스케줄러(Midium-term scheduler)`가 메모리에 올라온 프로세스 수(degree of Multiprogramming)를 조절하는 경우
    - swap out
        - 상태 변화: `Ready` 또는 `Blocked` -> `Suspended`
    - swap in
        - 상태 변화: `Suspended` -> `Ready` 또는 `Blockced`
    - `Suspended` 상태는 `Suspend Blocked`와 `Suspended Ready`로 나뉘는 걸로 추정
    - active와 inactive
        - active: swap in이 된 상태
        - inactive: swap out이 된 상태
        - 조금 더 조사가 필요하지만, active는 메모리가 부여된 상태이고 inactive는 메모리를 빼앗긴 상태로 추정
    
- Terminated
    - 프로세스의 모든 작업이 수행된 상태로, 후처리가 진행되는 상태이다.
    - exit
        - 상태 변화: `Running` -> `Terminated`

<br>

### 📚 참고 자료
- [KOCW 운영체제 - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
