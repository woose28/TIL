## 📌 가상 메리(Virtual Memory)

### 💡 사전 지식
1. Demand Paging
- 페이지에 대한 요청이 왔을 때(페이지를 사용할 때), 메모리에 페이지를 적재시키는 방법
    - I/O 양 감소
    - 메모리 사용량 감소
    - 빠른 응답시간 기대
    - 더 많은 사용자 수용 가능
- 대부분의 운영체제에서 페이징 기법을 사용한다.
- Demand Paging 기법에서는 `valid/invalid` bit를 사용
    - 처음에 페이징 테이블의 모든 엔트리의 `valid/invalid` bit는 모두 invalid이다.
    - invalid bit인 엔트리에 대해서 주소 변환을 시도하면 트랩이 걸리며 이를 `page fault`라고 한다.

2. 캐싱 기법(caching)
- 한정된 빠른 공간(저장 장치, 캐시)에 요청된 데이터를 저장했다가, 추후에 동일한 요청이 발생했을 때 캐시로부터 데이터를 제공하는 기법

3. 지역성(Locality)
- 프로세스가 특정 시간 동안 일정 장소의 메모리만 집중적으로 참조하는 성질
- 집중적으로 참조하는 페이지 집합을 locality set이라고 한다.

### ✔️ 페이지 부재(Page fault)
- invalid한 페이지에 접근할 때 MMU에서 trap을 발생시키고 이를 페이지 부재라고 한다.
- 처리 순서
    1. valid한 참조인지 확인
        - 참조한 주소가 올바른지 또는 protection 상태를 확인
    2. 물리 메모리의 빈 프레임을 하나 선정한다.(없으면 다른 프레임을 뺏는다.)
    3. 요청된 페이지를 Disk에서 memory로 읽어 온다.
        - 주소 변환을 요청한 프로세스는 CPU를 선점당한다.(Disk에서 읽어오는 작업은 커널이 수행)
        - Disk에서 메모리로 페이지를 읽어오는 작업이 끝나면, 페이지 테이블의 엔트리에 프레임 정보와 `valid/invalid` bit 정보를 기록
        - 주소 변환을 요청한 프로세스를 `준비 큐(ready queue)`로 옮긴다.
    4. 방금 주소 변환을 요청한 프로세스가 CPU 제어권을 다시 부여받으면, instruction을 다시 재개한다.

### ✔️ Page replacement
- 어떤 프레임을 빼앗을지 결정하는 것
- 바로 사용되지 않은 페이지의 프레임을 빼앗는 게 중요
    - 프레임을 빼앗긴 페이지는 Backing Store로 이동된다.
    - 프레임을 빼앗긴 페이지 엔트리의 `valid/invalid` bit를 invalid로 변경
    - 프레임을 부여받은 페이지 엔트리의 `valid/invalid` bit는 valid로 변경
- `page replace algorithm`은 `page-fault rate`를 최소화하는 것이 목표이다.
    - 즉 `page replace algorithm`은 성능 척도는 `page-fault`가 발생되는 횟수이다.

### Optimal Algorithm
- Offline algorithm, MIN, OPT라고도 불린다.
- 미래에 발생되는 페이지 참조 순서를 알고 있다는 가정하에, 가장 먼 미래에 참조되는 page를 교체한다.
    - 실제 시스템 환경에서 페이지 참조 순서를 예측하는 것은 어렵기 때문에 사용하기 적합하지 않다.
- Optimal Algorithm의 성능은 다른 어떤 알고리즘의 성능보다 좋다.
    - 다른 Algorithm의 성능의 upper bound를 제공한다.(비교 척도로 사용)

### FIFO(First In First Out) Algorithm
- 가장 먼저 들어온 페이지를 내보낸다.
- FIFO Anomaly(Belady's Anomaly)
    - 메모리 성능(프레임 수)를 증가시키면 간혹, 성능이 떨어지는 경우가 있다.(페이지 부재 횟수가 증가한다.)

### LRU(Least Recently Used) Algorithm
- 가장 오래전에 참조된 것을 지운다.
- 페이지 참조 순서를 Linked-List 형태로 관리한다.
    - 페이지 참조 순서를 변경하기 위해서 O(1) 시간이 소모된다.
        - 기존 페이지 중 다시 참조되는 페이지가 있다면 맨 앞으로 이동
        - 페이지 부재가 발생하면, 맨 뒤에 있는 페이지를 제거

### LFU(Least Frequently Used) Algorithm
- 참조 횟수가 가장 적은 페이지를 지운다.
- 최저 참조 횟수인 페이지가 여러 개인 경우
    - 최저 참조 횟수인 페이지 중 임의로 선정 또는 가장 오래전에 참조된 페이지를 선정
- `LRU` 알고리즘보다 페이지의 인기도를 더 정확히 반영할 수 있지만, 최근성은 덜 정확하다.
- 페이지 참조 순서를 Heap으로 구현한다.
    - 맨 위에 참조 횟수가 가장 적은 페이지를 저장한다.
    - 부모는 자식보다 참조 횟수가 적게 배치한다.
    - 페이지 참조 순서를 변경하기 위해서 O(log n) 시간이 소요된다.
    - 페이지 부재가 발생하면 루트 노드에 있는 페이지를 제거한다.

❗️ 실제 페이징 시스템에서는 `LRU`와 `LFU`를 적용시킬 수 없다.
- 프로세스에서 주소를 변환하고 메모리를 참조하는 동작은 OS의 도움 없이 가능하다.
- OS가 이 과정에 개입하는 경우는 페이지 부재가 발생할 때이다.
- 때문에 페이지 부재가 발생하지 않는다면 `LRU`와 `LFU` 알고리즘에서 사용하는 자료구조(Linked-List 또는 Heap) 자료 구조의 상태를 관리할 방법이 없다.

### Clock Algorithm
- `LRU`의 근사 알고리즘
- Second chance algorithm, NUR(Not used Recently), NRU(Not Recently Used) 라고도 불린다.
- 페이징 시스템에서 일반적으로 사용하는 알고리즘
- Reference bit를 이용한다.
    - Reference bit는 페이지를 참조할 때 하드웨어가 설정한다.
    - Reference bit이 1이면 최근에 해당 페이지가 참조된 것을 의미한다.
    - Reference bit이 0이면 최근에 해당 페이지가 참조되지 않았다는 것을 의미한다.
- 동작 원리
    - circular list를 이용해서 페이지 교체를 진행한다.
    - circular list의 특정 지점을 포인터라고 하며, 포인터의 위치부터 Reference bit를 확인한다.
        - Reference bit가 1이면 해당 값을 0으로 변경하고 포인터의 다음 위치로 이동한다.
        - Reference bit가 0이면 포인터에 위치에 해당하는 페이지를 교체한다.
    - 만약 현재 circular list에 존재하는 페이지의 참조가 발생하면, 해당 페이지의 Reference bit를 1로 변경한다.
- Modified bit도 함께 사용하는 방법도 있다.
    - Modified bit는 해당 페이지의 수정 여부를 표현한다.
    - Modified bit이 1이면 최근에 수정이 된 페이지를 의미한다.
        - 따라서 해당 페이지는 페이지 교체가 일어날 때, Backing Store에 따로 저장이 필요하다.
    - Modified bit이 0이면 최근에 수정이 발생하지 않은 페이지를 의미한다.
        - 따라서 해당 페이지는 페이지 교체가 일어날 때, 그냥 제거하면 된다.
    - 알고리즘의 성능을 높이기 위해서, Modified bit이 0인 페이지를 우선적으로 교체되게 구현할 수 있다.

<br>

### ✔️ Frame Allocation
- Allocation Problem
    - 각 프로세스에 어느 정도의 프레임을 할당한 것인가에 대한 문제
    - 할당된 프레임의 개수에 따라 페이지 부재의 횟수가 달라지게 된다.
- Allocation Scheme
    - Euqual allocation
        - 모든 프로세스에 같은 개수의 프레임을 할당
    - Proportional allocation
        - 프로세스의 크기에 비례해서 프레임을 할당
    - Priority allocation
        - 프로세스의 우선순위에 따라 프레임을 할당

### Global replacement
- 페이지 교체 시 다른 프로세스에 할당된 프레임을 뺴앗을 수 있는 방법
- 프로세스 별 할당량을 조절할 수 있는 방법 중 하나이다.
- Working-set Algorithm과 PFF가 여기에 해당

### Local replacement
- 자신에게 할당된 프레임 내에서만 프레임을 교체할 수 있는 방법
    - 사전에 미리 프로세스 별로 프레임을 할당해야 한다.

### Trashing 현상
- 프로세스가 원활하게 실행되기 위한 최소한의 메모리(프레임 수)를 할당받지 못해서 페이지 부재가 빈번히 발생되는 경우
    - 페이지 부재가 빈번히 발생
    - CPU utilization이 낮아짐
- 보통 `MPD(mutiprograming degree)`가 너무 높아졌을 때 발생한다.
    - `MPD`를 제한할 필요가 있다.

### Working-Set Model
- Locality를 기반으로 프로세스가 일정 시간 동안 원활하게 실행되기 위해 메모리에 적재돼 있어야 하는 페이지 집합을 working set이라고 한다.
- 동작 원리
    - 프로세스의 working set이 메모리에 모두 적재돼 있다면 실행
    - 그렇지 않다면, 현재까지 할당받은 메모리(프레임)를 반납하고 `swap out`된다.
- Trashing 현상을 방지한다.
- Mutiprogramming degree를 결정한다.

### Working-Set Algorithm
- 프로세스의 Working-Set을 미리 예측하는 것은 어렵다.
- Working-Set을 활용하기 위해서 과거 참조 기록을 이용한다.
- Workging-set window
    - Working-Set을 구성하기 위해 과거 참조할 기록의 개수
    - Workging-set window가 10이면 현재 시점을 기준으로 과거 10개의 기록의 참조해서 Working-set을 구성한다.
    - window size 크기
        - window size가 너무 작으면 locality set을 모두 수요하지 못할 가능성이 있다.
        - window size가 너무 크면 여러 규모의 locality set을 수용하게 된다.
        - 따라서 적당한 크기의 window size를 결정해야 한다.
- Working-set은 현재 시점부터 과거까지(현재를 기준으로 window의 크기만큼 전까지)의 기록 중 서로 다른 페이지들로 구성한다.(set 자료구조를 생각!)
    - 만약 Working-set의 크기가 5인 상태라면, 해당 프로세스는 5개의 프레임이 할당됐을 때 실행된다.
    - 만약 5개 미만의 프레임이 할당됐다면, 해당 프로세스는 현재 보유하고 있는 프레임을 모두 반납하고 `swap out`된다.
- Working-set은 시간의 흐림에 따라 변한다.
    - 즉, 프로세스가 실행되기 위해 필요로 하는 프레임의 수도 변한다.
- Working-set 알고리즘은 `MPD`를 조절할 수 있다.
    - 프로세스들의 working set size 합 < page frame 수
        - 일부 프로세스들을 `swap out` 시킨다.
        - 남은 프로세스들에게 프레임을 할당시켜 우선적으로 실행한다.
        - 결과적으로 `MPD`를 감소시키는 것이다.
    - 프로세스들의 working set size 합 > page frame 수
        - `swap out`된 프로세스에게 프레임을 할당한다.
        - `MPD`를 증가시키는 효과


### Page-Fault Frequency(PFF) Scheme
- page-fault rate의 상한값과 하한값을 결정한다.
    - 현재 프로세스의 page-fault rate < 상한값
        - 현재 프로세스에 프레임을 더 할당한다.
        - 만약 빈 프레임이 없으면, 다른 프로세스 `swap out` 시켜서 프레임을 확보한다.
    - 현재 프로세스의 page-fault rate > 하한값
        - 현재 프로세스에 할당된 프레임을 회수한다.

<br>

### Page size 결정
- Page size가 작으면 발생되는 현상
    - 페이지 수 증가
    - 페이지 테이블 크기 증가
    - 내부 단편화 감소
    - 디스크에서 데이터를 찾는 과정이 시간이 오래 걸린다.
        - 페이지 크기가 작으면 비교적 빈번히 디스크를 참조하기 때문에 비효율적이다.
    - 필요한 정보만 메모리에 올라와 메모리 이용률 증가
    - Locality의 활용 측면에서는 좋지 않음
- 최근에는 페이지 사이즈를 증가시키는 것이 추세이다.

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Virtual Memory - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

<br>

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
