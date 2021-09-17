# Baekjoon_10814
# 나이순 정렬

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad31eb73-2b7f-4a73-8664-9e70c56207a3/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad31eb73-2b7f-4a73-8664-9e70c56207a3/Untitled.png)

## 문제

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

## 출력

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

## 예제 입력 1

```
3
21 Junkyu
21 Dohyun
20 Sunyoung

```

## 예제 출력 1

```
20 Sunyoung
21 Junkyu
21 Dohyun
```

---

### 풀이

문제에 나와있는 조건에 맞게 데이터를 정렬 후 출력하면 되는 문제이다.

나이가 같은 회원들의 경우 가입한 순서로 정렬을 해야하므로 정렬할 때 데이터의 인덱스를 사용했다.

```python
N = int(input())

members = []

for idx in range(N):
	age, name = input().split()
	age = int(age)
	members.append((age, idx, name))

members = sorted(members, key=lambda x : x[0])

for member in members:
	print(member[0],member[2])
```

위 문제는 실행 시간이 약 4500ms 이다.

이 풀이에서 입력 부분을 input() 함수 대신 stdin.readline()을 사용하면 실행속도가 많이 줄어드는 효과를 확인 할 수 있다.

```python
from sys import stdin

N = int(stdin.readline())

member_list = []

for idx in range(N):
	age, name = stdin.readline().split()
	member_list.append((int(age), idx, name))

member_list.sort(key=lambda x : x[0])

print("\n".join([str(m[0])+" "+m[2] for m in member_list]))
```

이 코드의  실행 시간은 256ms 이다.

이 문제를 통해

1. 입력에 소요되는 시간을 줄이기 위해 stdin.readline() 사용하기
2. 문자열로 답을 출력할 때 join()을 이용하여 코드의 양 줄이기

위 두가지 사항을 알게되었다.

---

### 출처

문제 출처

[https://www.acmicpc.net/problem/10814](https://www.acmicpc.net/problem/10814)

풀이 참고

백준 체점번호 - 22658976
