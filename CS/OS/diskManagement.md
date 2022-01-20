## 📌 디스크 관리(Disk Management)

### ✔️ 디스크 구조
- logical block
    - 디스크 외부에서 보는 디스크의 단위 정보 저장 공간
    - 주소를 가진 1차원 배열처럼 취급
    - 정보를 전송하는 최소 단위
- sector
    - logical block이 물리적인 디스크에 매핑되는 위치
    - Sector 0는 최외곽 실린더의 첫 트랙에 있는 첫 번째 섹터이다.
        - Sector 0에는 부팅과 관련된 정보가 담겨있다.

<br>

### ✔️ 디스크 관리
- physical formatting(=low-level formatting)
    - 디스크를 컨트롤러가 읽고 쓸 수 있도록 섹터들로 나누는 과정
    - 각 섹터는 header + 실제 data(보통 512byte) + trailer로 구성
        - header와 trailer에는 sector number, ECC(Error-Correcting Code) 등의 부가적인 정보가 저장된다.
        - ECC는 저장되는 데이터의 축약본으로, sector에 저장된 내용에 오류가 없는지 확인하기 위해 사용된다.
- Partitioning
    - 디스크를 하나 이상의 실린더 그룹으로 나누는 과정
    - OS는 이 파티션을 독립적인 disk로 취급한다.(logical disk)
- Logical formatting
    - 파일 시스템을 만드는 것
    - FAT, inode, free sapce 등의 구조 포함
- Booting
    - ROM에 있는 `small bootstrap loader`의 실행
        - 컴퓨터 전원을 키면 CPU 제어권이 ROM의 주소를 가리킨다.
        - ROM에 있는 `small bootstrap loader`이 실행됨(명령문처럼)
        - 그 후 하드디스크의 0번 sector에 있는 내용을 메모리에 올려 실행 시킨다.
        - sector 0에는 boot block이 저장되어 있다.
        - boot block은 파일 시스템에서 운영체제 커널 위치를 찾아서 메모리에 올려 실행되게 한다.
    - sector 0(boot block)은 `full Bootstrap loader program`

<br>

### ✔️ 디스크 스케줄링
- Access time
    - 크게 세 가지 시간 요소가 있다.
    - Seek time
        - 헤드를 해당 실린더로 움직이는 데 걸린 시간
            - 디스크의 성능을 높이기 위해서 Seek time을 줄이는 게 중요하다.
        - Access time에서 가장 많은 부분을 차지한다.
            - 물리적인 기계를 움직이는 과정
    - Rotational latency
        - 헤드가 원하는 섹터에 도달하기까지 걸리는 회전 지연 시간
    - Transfer time
        - 실제 데이터의 전송 시간
        - 굉장히 작은 시간을 차지한다.
- Disk bandwidth
    - 단위 시간당 전송되는 바이트 수
    - 디스크의 성능을 나타낸다.
- Disk Scheduling
    - seek time을 최소화하는 것이 목표
    - seek time은 보통 seek distance와 비례하는 성향이 있다.

<br>

### ✔️ 디스크 스케줄링 알고리즘(Disk Scheduling Algorithm)
- seek time을 최소화하기 위해 disk에 요청 사항을 바로 처리하는 것이 아니라, seek distance가 작아지도록 요청 사항을 처리한다.
- 디스크 스케줄링 알고리즘은 seek time을 최솨화하기 위해 disk에 들어온 작업을 처리하는 순서를 결정하는 방법
- 종류
    - FCFS(First Come First Service)
    - SSTF(Shortest Seek Time First)
    - SCAN
    - C-SCAN
    - N-SCAN
    - LOOK and C-LOOK
- 기본적으로 디스크 스케줄링 알고리즘은 SCAN 기반의 알고리즘을 이용한다.

### FCFS(First come First Service)
- 요청이 들어온 순서대로 처리한다.

### SSTF(Shortest Seek Time First)
- 현재 헤더에서 가장 가까운 위치의 요청부터 처리한다.
- `기아 현상(starvation)`이 발생할 수 있다.

### SCAN
- 엘리베이터의 동작 방식과 유사하다.
- disk arm이 디스크 한쪽에서 끝에서 다른 쪾 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리한다.
- 한쪽 끝에 도달하면 반대 반향으로 이동하면서 들어온 요청을 처리한다.
- 실린더 위치에 따라 대기 시간이 다른 단점이 있다.
    - 실린더 위치가 중앙에 있다면 최악의 경우 반 바퀴만 기다리면 된다.
    - 실린더 위치가 끝에 있다면 최악의 경우 한 바퀴를 기다려야 한다.

### C-SCAN
- disk arm이 디스크 한쪽에서 끝에서 다른 쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리한다.
- 한쪽 끝에 도달하면 요청을 처리하지 않으면서 출발 위치로 다시 이동한다.
- SCAN보다 균일한 대기 시간을 제공한다.

### N-SCAN
- SCAN의 변형 알고리즘
- disk arm이 이동하기 전에 들어온 요청은 한쪽 방향으로 움직이며 처리하지만, 이동하는 도중에 들어오는 요청은 다음 번 이동에 처리하는 방법

### LOOK and C-LOOK
- LOOK은 SCAN의 변형 알고리즘
- C-LOOK은 C-SCAN의 변형 알고리즘
- LOOK 방식은 한쪽 방향으로 요청을 처리를 하며 진행하지만, 이동 방향의 다음 위치에 요청이 없으면 반대로 방향을 회전하는 방식이다.
    - 진행 방향의 다음 위치에 요청이 없어도 다른 쪽 끝까지 진행하는 SCAN과 C-SCAN 방식과 차이가 있다.

<br>

### ✔️ 스왑 공간 관리(Swap-Space Management)
- Disk를 사용하는 두 가지 이유
    - 비휘발성, 데이터의 영속성
        - 따라서 file system을 사용한다.
    - 프로그램 실행을 위한 메모리 공간의 부족
        - 따라서 swap space를 사용한다.
- Swap-space
    - Virtual memory system에서는 디스크를 메모리의 연장 공간으로 사용한다.
    - 파일 시스템 내부에 둘 수 있으나, 보통 별도의 partition에 사용하는 것이 일반적이다.
        - 공간 효율성보다 속도 효율성이 우선된다.
        - 일반 파일보다 훨씬 짧은 시간만 존재하고 자주 참조된다.
            - block의 크기 및 저장 방식이 일반 파일시스템과 다르다.

<br>

### ✔️ RAID(Redundant Array of Independent Disks)
- 여러 개의 디스크를 묶어서 사용
- 사용 목적
    - 디스크 처리 속도 향상
        - 여러 디스크에 block의 내용을 분산 저장
        - 병렬적으로 데이터를 읽어온다.(interleaving 또는 striping이라고 한다.)
    - 신뢰성(reliability) 향상
        - 동일 정보를 여러 디스크에 중복 저장
        - 하나의 디스크가 고장 나면 다른 디스크에서 데이터를 읽어온다.(mirroring 또는 shadowing이라고 한다.)
        - 단순히 중복 저장이 아니라 일부 디스크에 parity를 저장하여 공간의 효율성을 높일 수 있다.
            - 오류 발생 여부를 확인하거나 에러를 복구할 수 있는 정도의 데이터만 저장한다.
    
<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Disk Management - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

<br>

<img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />