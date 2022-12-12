## 📌 프로세스 생성(Process Creation)

### 💡 사전 지식
1. `init` 프로세스는 모든 프로세스의 부모 프로세스이다.
2. 일반적으로 부모 프로세스가 종료되기 전, 그 자식 프로세스들이 먼저 종료돼야 한다.
3. 부모 프로세스와 자식 프로세스가 자원을 공유하는 방식은 여러 가지가 있다.
    - 부모 프로세스와 자식 프로세스가 모든 자원을 공유하는 모델
    - 부모 프로세스와 자식 프로세스가 일부 자원을 공유하는 모델
    - 부모 프로세스와 자식 프로세스가 전혀 자원을 공유하지 않는 모델

<br>

### 💻 대표적인 프로세스 관련 시스템 콜(Syatem Call)
1. fork()
2. exec()
3. wait()
4. exit()
5. abort()

<br>

### 1. fork()
- 프로세스의 메모리 영역을 복제하는 시스템 콜
- 생성된 자식 프로세스는 부모 프로세스와 동일한 메모리 영역을 가지고 있다.
    - code, data, stack 영역을 모두 복사
- 예제 코드
```c
int main() {
	int pid;
	pid = fork();

	if (pid == 0) {
		printf("\n Hello. I am child!\n");
	} else if (pid > 0) {
		print("\n Hello, I am parent!\n");
	}
}
```
- 자식 프로세스는 부모 프로세스의 `PC(Program Counter)` 값 또한 복사하기 때문에, `fork()` 함수 이후부터 실행된다.
- `fork()` 함수의 반환 값으로 부모 프로세스와 자식 프로세스를 구분한다.
    - 부모 프로세스: fork()의 반환 값으로 양수가 반환된다.(자식 프로세스의 pid)
    - 자식 프로세스: fork()의 반환 값으로 0이 반환된다.
    - 만약, `fork()` 함수 실행이 실패하면(메모리 부족 또는 생성된 프로세스가 너무 많을 때) -1을 반환한다.

<br>

### 2. exec()
- 할당된 메모리 공간에 새로운 프로그램을 올린다.
- `exec()` 시스템 콜을 실행하면 메모리에 새로운 프로그램 코드가 올라오므로, 이전 프로그램의 코드는 실행할 수 없다.
    - 즉, `fork()` 시스템 콜로 복제한 부모 프로세스 코드를 `exec()` 시스템 콜 이후에는 실행할 수 없다.
- 예제 코드
```c
int main() {
	int pid;
	pid = fork();

	if (pid == 0) {
		printf("\n Hello. I am child! Now I'll run date\n");
		execlp("/bin/date", "/bin/date", (char*) 0);
	} else if (pid > 0) {
		print("\n Hello, I am parent!\n");
	}
}
```
- `execlp()`함수는 `exec()` 시스템 콜을 하게된다.


<br>

### 3. wait()
- `wait()` 시스템 콜은 보통 부모 프로세스가 자식 프로세스를 생성하면서 호출한다.
    - 자식 프로세스가 종료될 때까지 기다리는 시스템 콜
    - 자식 프로세스가 실행되면 부모 프로세스는 sleep이 된다.(`Block` 상태가 됨)
    - 자식 프로세스가 종료되면 부모 프로세스는 `Ready` 상태가 된다.
    - 덕분에, 부모 프로세스와 자식 프로세스가 CPU 제어권을 얻기 위해 경쟁하지 않아도 된다.

- 예제 코드
```c
main() {
	int childPID;

	childPid = fork();


	if (childPid == 0) {
		/* code for child process */
	} else {
		wait();
	}
}
```

<br>

### 4. exit()
- 프로세스가 자발적으로 종료되는 경우 `exit()` 시스템 콜을 호출한다.
- 프로세스에 할당된 자원의 반납을 요청하고, 부모 프로세스에게 종료되는 것을 알리는 시스템 콜이다.
- 명시적으로 `exit()` 시스템 콜을 할 수도 있고, main() 함수가 리턴되는 위치에 컴파일러가 `exit()` 시스템 콜을 호출할 수도 있다.

<br>

### 5. abort()
- 프로세스가 비자발적으로 종료되는 경우에 해당되는 시스템 콜이다.
- 비자발적인 종료는 아래의 경우가 있다.
    - 부모 프로세스가 자식 프로세스를 강제 종료시킴
        - 자식 프로세스가 할당된 자원 이상의 자원을 사용하는 경우
        - 자식 프로세스의 작업이 더 이상 의미 없는 경우
    - 사용자가 강제로 프로세스를 종료 시킨 경우
    - 부모 프로세스가 종료하는 경우
        - 부모 프로세스를 종료하기 전에 자식 프로세스를 먼저 종료시킨다.


<br>

### 📚 참고 자료
- [KOCW 운영체제 Ch.Process Management - 반효경 교수님](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
