## 📌 스레드(Thread)

### 💻 스레드란?
- CPU 작업을 수행하는 단위로 하나의 프로세스에서 독립적인 작업 흐름을 가진다.
- 하나의 프로세스 안에는 여러 개의 스레드가 존재할 수 있다.
    - 각각의 스레드는 독립적인 작업 흐름을 가진다.
- 스레드는 프로세스의 주소 공간과 자원을 공유한다.
    - 따라서 동일한 작업을 여러 프로세스를 생성해서 수행하는 것보다, 하나의 프로세스 안에 여러 스레드로 나눠서 수행하면 메모리 측면에서 이점이 있다.
- 스레드는 스레드 ID, stack, PC counter, 레지스터 집합을 독립적으로 가진다.
    - 독립적인 stack 영역 덕분에 스레드는 독립적인 실행흐름을 가질 수 있다.
    - 독립적인 PC counter와 레지스터 집합 덕분에 스레드는 CPU를 스케줄러에 의해 선점 당해도 독립적으로 작업 내용을 저장할 수 있다.

<br>

### 멀티 스레드
- 하나의 프로세스의 작업을 여러 스레드로 나눠서 수행하는 방법
- 동일한 프로세스 안에 있는 스레드들은 프로세스의 메모리 영역(Code, Data, Heap 영역)을 공유하는 장점이 있지만, 문제점도 존재한다.

<br>

### ✔️ 멀티 스레드의 장점
- 스레드 사이의 context switch 비용은 프로세스 사이의 context switch 비용보다 낮기 때문에 동일한 작업을 여러 프로세스로 나눠서 수행하는 것보다, 하나의 프로세스에서 여러 스레드로 나눠서 하면 overhead가 줄어들게 된다.
    - 프로세스의 contextx switch는 cache-memory를 비우는 작업이 필요한 반면, 스레드의 경우 해당 작업이 필요하지 않다.

- 하나의 프로세스 안에 있는 스레드들은 프로세스의 메모리 영역을 공유하기 때문에, 여러 프로세스를 생성하는 것보다 하나의 프로세스에 여러 스레드를 생성하는 것이 메모리 측면에서 이점이 있다.
    - 또한, 프로세스 사이의 통신보다 스레드 사이의 통신이 더욱 간결하다.(스레드는 공유 공간에 있는 데이터를 참조하고 이용하면 된다.)

### ❗️ 멀티 스레드의 문제점
- 멀티 스레드를 사용한다면, 공유되는 공간과 자원이 생길 수 있다. 따라서, 공유되는 자원에 대해서 동기화 작업이 필요하다.
    - 이러한 동기확 작업은 자원에 접근하는 스레드의 순서를 통제하는 것으로, 너무 과도한 락은 병목현상을 초래하여 성능이 오히려 저하될 수 있다.

<br>

### ✔️ 스레드의 종류
1. 커널 수준 스레드(kernel level thread)
    - 운영체제가 지원하는 스레드 기능을 통해 생성된 스레드
    - 커널이 스레드를 생성하고 스케줄링 한다.
        - 스레드를 관리하기(스케줄링 또는 동기화) 위해서 system call을 한다.(즉, 유저 모드와 커널 모드 간 전환이 존재한다.)
        - 따라서, overhead가 상대적으로 크다.
        - 프로세스 내의 스레드 1개당 커널 스레드 1개를 할당한다.
        - 커널이 스레드 정보를 관리한다.(PCB와 TCB 모두 커널이 관리한다.)
        - 커널이 개별적인 스레드를 관리하기 때문에, 하나의 스레드에서 system call이 발생해도 동일 프로세스 내의 다른 스레드는 계속 실행 될 수 있다.


2. 사용자 수준 스레드(user level thread)
    - 사용자 레벨의 라이브러리를 통해 생성된 스레드
    - 라이브러리가 스레드를 생성하고 스케줄링한다.
        - 스레드를 관리하기(스케줄링 또는 동기화) 위해서 system call을 하지 않는다.(즉, 유저 모드와 커널 모드 간 전환이 없다.)
        - 따라서, 커널의 도움 없이 스레드를 관리하기 때문에 overhead가 적음
        - 커널은 스레드의 존재를 모르기 때문에 하나의 프로세스로 바라본다.(PCB만 커널에서 관리하고 TCB는 프로세스 내에서 관리한다.)
        - 따라서, 하나의 스레드가 system call을 하면 해당 프로세스의 모든 스레드가 중단된다.(동기식)

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Process 2 - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
- [Interview_Question_for_Beginnner - Part 1-4 운영체제](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/OS#스레드thread)
- [커널 레벨 쓰레드와 유저 레벨 쓰레드](https://kspsd.tistory.com/m/50#)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
