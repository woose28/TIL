## 📌 CPU 스케줄링(CPU Scheduling)

### 💡 사전 지식
1. CPU burst와 I/O burst
    - 프로세스가 실행되는 동안 `CPU burst`와 `I/O burst`가 반복된다.
    - CPU burst time
        - CPU를 연속적으로 사용하는 시간
    - I/O burst time
        - I/O 작업을 기다리는 시간
        - 이 시간동안은 CPU를 사용하지 못한다.(CPU가 낭비됨)

2. CPU 스케줄러(Scheduler)와 디스패처(Dispatcher)
    - CPU 스케줄러
        - 준비 큐(Ready Queue)에 있는 프로세스 중에서 CPU 제어권을 넘겨 줄 프로세스를 선택한다.
    - 디스패처
        - `CPU 스케줄러`에 의해 선택된 프로세스에게 CPU 제어권을 넘겨준다.
        - `문맥 교환(Context Switch)`를 담당한다.
            - 이전 프로세스(P0)의 작업 내용을 P0의 PCB에 저장하고, 다음 프로세스(P1)의 작업 내용을 P1의 PCB에서 불러온다.
            - 이 시간을 `디스패치 지연(Dispatch latency)`라고 한다.

3. CPU 스케줄링 알고리즘은 크게 두 종류로 나뉜다.
    - 선점형 알고리즘(preemptive)
    - 비선점형 알고리즘(nonpreemptive)

<br>

### ✔️ CPU 스케줄링을 하는 이유
- 컴퓨터의 중요한 자원인 CPU를 효율적으로 사용하기 위해서 CPU 스케줄링을 한다.

<br>

### ✔️ CPU 스케줄링 척도(기준)
- 시스템 입장에서의 성능 척도
    - CPU utilization(CPU 이용률)
        - 전체 시간 중 CPU가 사용된 시간의 비율
        - CPU utilization을 큰 게 좋다.
    
    - Throughput(처리량)
        - 주어진 시간동안 완료한 작업의 수
        - 즉, 단위 시간동안 완료한 프로세스의 개수
        - Throughput 또한 큰 게 좋다.

- 프로세스 입장에서의 성능 척도
    - Turnaround time(총 처리 시간)
        - 프로세스가 준비 큐에 들어와서 실행이 완료될 때까지 걸린 시간
        - Turnaround time은 작은 게 좋다.
    
    - Waiting time(대기 시간)
        - 프로세스가 준비 큐에서 대기하는 시간의 총 합
        - Waiting time은 작은 게 좋다.

    - Response time(응답 시간)
        - 준비 큐에 들어와서 처음 CPU를 얻을 때까지 소요되는 시간
        - 대화식 프로그램(interactive program)에서는 응답 시간이 중요할 수 있다.

<br>

### ✔️ CPU 스케줄링 알고리즘 종류
1. FCFS(First-Come First-Served)
    - 비선점형 스케줄링
    - 준비 큐에 도착한 프로세스 순서대로 CPU 제어권을 부여한다.
    - 경우에 따라 `평균 대기 시간`이 상대적으로 길어질 수 있다.
        - CPU 사용 시간이 긴 프로세스들이 CPU 사용 시간이 짧은 프로세스들 보다 먼저 도착하면, CPU 사용 시간이 짧은 프로세스들은 대기해야 한다.
        - `호위 효과(Convoy Effect)`가 발생할 수 있다.
            - `호위 효과`
                - 다른 모든 프로세스 들이 CPU 사용 시간이 긴 프로세스가 CPU를 양도하기를 기다리는 현상
            
2. SJF(Shortest-Job-First)
    - 각 프로세스의 다음 번 `CPU burst time`을 가지고 스케줄링에 활용
    - `CPU burst time`이 가장 짧은 프로세스를 제일 먼저 스케줄링
    - 비선점형과 선점형으로 나뉜다.
        - 비선점형(nonpreemptive)
            - CPU 제어권을 부여받으면, 현재 CPU burst tmie이 끝날때까지 CPU를 사용한다.
            - CPU 제어권을 부여받은 프로세스의 CPU burst time이 끝날때마다 CPU 스케줄링을 한다.
        - 선점형(preemptive)
            - 현재 실행 중인 프로세스의 남은 CPU burst time보다 더 짧은 CPU burst time을 가지는 프로세스가 도착하면 CPU 제어권을 빼앗아서 새로 도착한 프로세스에게 할당한다.
            - 이 방법을 `SRTF(Shortest-Remaining-Time-First)`라고 한다.
            - 새로운 프로세스가 도착할 때마다 CPU 스케줄링을 한다.
    - 평균 대기 시간을 최소화한다.(특히, 같은 상황에서 SRTF 알고리즘이 평균 대기시간이 가장 짧다.)
    - 문제점
        - 기아 현상(Starvation)
            - `CPU burst time`이 긴 프로세스는 CPU를 제어권을 받는 우선순위에서 밀린다.
            - 이를 해결하기 위해 `aging(노화)` 기법이 있다.
                - 오래 기다린 프로세스는 우선 순위를 높이는 방법이다.

        - 실제 시스템에서 `CPU burst time`을 정확히 계산하기 힘들다.
            - 다만, 예측(추정)을 할 수 있다.(과거 사용 기록을 기반으로)
            - 과거의 `CPU burst time`을 이용해서 추정

3. Priority Scheduling
    - 우선순위가 높은 프로세스에게 CPU 제어권을 부여하는 방법
        - 우선순위가 같은 프로세스에 한해서는 `FCFS` 방식으로 스케줄힌다.
    - 비선점형과 선점형으로 나뉜다.
    - 보통 우선순위는 정수로 표현하며, 운영체제에서 낮은 정수가 높은 우선순위를 가진다.
        - 그렇지 않은 시스템도 존재할 수 있다.
    - `SJF`는 일종의 Priority scheduling이다.
    - 문제점
        - 기아 현상(Starvation)

4. Round Robin(RR)
    - 선점형 스케줄링
    - 현대 시스템은 RR을 기반의 스케줄링 기법을 사용한다.
    - 각 프로세스는 동일한 크기의 `할당 시간(time quantum, time slice)`을 가지고 있다.
        - 할당 시간을 모두 사용하면, CPU 제어권을 선점 당한다.
        - 할당 시간을 모두 사용하면, `intterupt`를 걸도록 타이머(timer)를 설정한다.
    - `RR`의 장점은 응답 시간이 짧다는 것이며, CPU burst time을 예측할 필요가 없다.
        - 큐에 n 개의 프로세스가 있고 할당된 시간이 t 일 때, 어느 프로세스도 (n-1)t 이상 기다리지 않는다.
    - `RR`의 성능은 `할당 시간`에 영향을 많이 받는다.
        - 할당 시간을 너무 길게 잡으면 FCFS와 비슷하게 된다.
        - 할당 시간이 너무 짧으면, `context switch`가 빈번하게 발생한다.(overhead 때문에 전체 시스템 성능이 떨어질 수 있다.)
    - 일반적으로 `SJF`보다 대기 시간과 반환 시간은 길지만, 응답 시간을 짧다.
    - CPU 사용 시간이 다양한 프로세스가 많을 때 사용하기 적합한 방법(CPU 사용시간이 짧은 프로세스와 긴 프로세스가 섞여 있을 때 적합)

5. Multilevel Queue Scheduling(다단계 큐 스케줄링)
    - 프로세스가 대기하는 큐가 여러 개 존재하며, 각 큐의 우선순위는 다르다.
    - 우선순위가 높은 큐에 있는 프로세스들에게 먼저 CPU를 할당한다.
    - 각 큐는 독립적인 스케줄링 알고리즘을 가질 수 있다.
    - 프로세스 유형에 따라 큐를 구별해서 구현할 수 있다.
        - Q0에는 대화형 프로세스를 대기시키고, Q1에는 배치 프로세스(계산 위주의 프로세스)를 대기시킨다.
        - Q0의 우선순위를 Q1의 우선순위보다 높게 설정한다.
    - 각 큐에 대해 스케줄링 구현 방법은 아래의 방법들이 있다.
        - Fixed Priority Scheduling
            - 우선순위가 높은 큐에 프로세스가 대기 중이면, 우선순위가 낮은 큐의 프로세스들은 CPU를 할당받지 못한다.
            - 기아 현상이 발생할 수 있다.
        - Time Slice
            - 각 큐에 CPU 시간을 적절히 할당하는 방식
            - ex. Q0에 80% 시간을 할당하고, Q1에 20% 시간을 할당한다.

6. Multilevel Feedback Queue Scheduling(다단계 피드백 큐 스케줄링)
    - `다단계 큐 스케줄링` 처럼 프로세스가 대기하는 큐가 여러 개 존재하지만, 차이점은 프로세스가 다른 큐로 이동이 가능하다는 점이다.
    - `다단계 피드백 큐 스케줄링` 알고리즘을 구현하기 위해 결정해야 하는 사항은 아래와 같다.
        1. 큐의 개수
        2. 각 큐의 알고리즘
        3. 프로세스의 우선순위를 높이고, 낮추는 기준
        4. 처음 프로세스를 할당한 큐의 기준
    - `다단계 피드백 큐 스케줄링` 알고리즘도 각 큐 별로 독립적인 스케줄링 알고리즘을 가질 수 있다.
        - 같은 `RR` 알고리즘을 사용하더라도, `time slice`의 크기가 다를 수 있다.

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch. CPU Scheduling 1 - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
- 운영체제 Ch.5 CPU 스케줄링 - Abraham Silberschatz 외 2인

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
