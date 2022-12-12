## 📌 입출력 종류

### 💻 입출력 종류
1. 동기식(Synchronous) 입출력
    - 프로세스가 입출력(I/O) 작업을 요청하면, 요청한 I/O 작업이 끝날 때까지 다음 명령문을 실행하지 않는 방식
    - 구현 방법
        - Non-blocking
            - I/O를 기다리는 동안, I/O를 요청한 프로세스가 CPU를 선점하고 있음
            - 따라서 프로세스가 요청한 작업이 완료될 때까지 CPU가 낭비된

        - Blocking
            - 프로세스에 의해 I/O 작업이 요청되면, 해당 프로세스의 상태를 `Blocked` 상태로 전환
            - CPU 제어권은 다른 프로세스에게 이양

2. 비동기식(Asynchronous) 입출력
    - 프로세스가 I/O 작업을 요청하고 요청한 작업이 완료될 때까지 기다리는 것이 아니라, 입출력과 관련 없는 다른 작업을 먼저 수행하는 방식
    - 요청한 I/O 작업이 끝나면, 입출력과 관련된 작업을 실행


동기식/비동기식 입출력 모두 입출력 작업이 끝나면 `interrupt`가 발생한다.

<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Process 2 - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)
- [sparkbosing - 입출력 구조](https://velog.io/@sparkbosing/입출력-구조)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
