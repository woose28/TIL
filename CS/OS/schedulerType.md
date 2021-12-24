## 📌 스케줄러(Scheduler) 종류

### 💡 사전 지식
1. 프로세스를 스케줄링 하기 위한 큐(Queue)의 종류
    - Job Queue: 현재 시스템에 있는 모든 프로세스의 집합
    - Ready Queue: 현재 메모리에 있으면서 CPU 제어권을 받기를 기다리는 프로세스 집합
    - Devices Queue: I/O Device의 처리를 기다리는 프로세스 집합

<br>

### ✔️ 스케줄러 종류
- 장기 스케줄러(Long-term scheduler or job scheduler)
    - 메모리를 부여할 프로세스를 결정하는 스케줄러(=어느 프로세스를 `Ready` 상태로 바꿀지 결정)
    - 메모리와 디스크 사이의 스케줄링을 한다.
    - 메모리를 부여받은 프로세스는 `Ready Queue`로 이동한다.
    - 메모리에 올라가 있는 프로세스의 수(degree of Multiprogramming)를 결정
    - `time sharing system`에는 장기 스케줄러가 보통 없다.(프로세스는 무조건 `Ready` 상태로 간다.)

- 단기 스케줄러(Short-term scheduler or CPU scheduler)
    - `Ready Queue`에 있는 프로세스 중 CPU 제어권을 넘겨 줄 프로세스를 결정하는 스케줄러(=어느 프로세스를 `Running` 상태로 바꿀지 결정)
        - `Ready Queue` 프로세스가 있다는 것은, 해당 프로세스는 메모리를 할당 받았다는 것이다.
    - 메모리와 CPU 사이의 스케줄링을 한다.

- 중기 스케줄러(Midium-term scheduler or Swapper)
    - 메모리의 여유 공간을 확보하기 위해 메모리를 빼앗을 프로세스를 결정하는 스케줄러(=어느 프로세스를 `Suspended` 상태로 바꿀지 결정)
    - 메모리에 올라가 있는 프로세스의 수(degree of Multiprogramming)를 결정
    - 프로세스로부터 메모리를 뺴앗는 과정을 `Swapping`이라고 한다.
        - 메모리를 빼앗기면 `swap out`, 메모리를 다시 부여받으면 `swap in`이라고 한다.

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Process 1 - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
