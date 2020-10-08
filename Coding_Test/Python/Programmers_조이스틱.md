# Programmers_조이스틱

### **문제 설명**

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

`▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동`

예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

`첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.`

만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

### 제한 사항

- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

### 입출력 예

name = "JEROEN" : return = 56

name = "JAN" : return = 23

---

### 풀이

조이스틱을 움직이는 경우는 2가지로 나뉜다.

1. 해당 칸의 알파벳을 변경하는 경우
2. 칸을 이동하는 경우

1의 경우 미리 알파벳 별 조이스틱 조작 횟수를 정의하면 쉽게 해결된다.

2의 경우 다음 등장하는 알파벳, 알파벳 변경 여부 등을 확인한 후 조작 횟수를 구했다.

```python
def solution(name):
    answer = 0
    pos = 0
    direct = 1
    length = len(name)
    check = [False] * length
    ref = "A"*length
    alpha = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":12, "P":11, "Q":10, "R":9, "S":8, "T":7, "U":6, "V":5, "W":4, "X":3, "Y":2, "Z":1}


    while(True):
        answer += alpha[name[(pos)%length]]
        ref = "".join([name[i] if i == pos%length else ref[i] for i in range(length)])

        check[(pos)%length] = True

        if(name == ref): break

        elif(name[(pos+direct)%length] != "A"):
            answer += 1
            pos += direct

        else:
            #정뱡향
            moving_cnt_01 = 1
            next_pos_01 = pos+direct
            while(True):
                if((pos)%length == (next_pos_01)%length):
                    break
                if(name[next_pos_01%length] != "A" and check[next_pos_01%length] == False):
                        break    
                moving_cnt_01 += 1
                next_pos_01 += direct    
            #역방향
            moving_cnt_02 = 1
            next_pos_02 = pos+(direct*-1)
            while(True):
                if((pos)%length == (next_pos_02)%length):
                    break
                if(name[next_pos_02%length] != "A" and check[next_pos_02%length] == False):
                    break
                moving_cnt_02 += 1
                next_pos_02 += (direct*-1)

            if(moving_cnt_01 <= moving_cnt_02):
                pos = next_pos_01
                answer += moving_cnt_01

            else:
                pos = next_pos_02
                answer += moving_cnt_02
                direct *= -1

    return answer
```
★**칸 이동 결정 방법**

변수

- answer : 조이스틱 동작 횟수
- direct : 움직이는 방향
- pos : 배열에서 현재 위치
- length : 배열 길이

원리

- direct 방향으로 한칸 움직였을 때 "A"가 아닌 경우

    조이스틱 동작 횟수 1증가 하고 이동

- 다음 문자가 "A"인 경우
direct 방향으로 A가 아닌 문자가 나올때 까지 이동 후 동작 횟수를 moving_cnt_01에 저장
동일한 원리로 direct 반대 방향으로 작업 수행 후 moving_cnt_02에 저장

    moving_cnt_01과 moving_cnt_02를 비교해서 더 작은 횟수를 answer에 더하고 더 작은 방향으로 direct 결정

---

### 참고 사항

아래의 코드는 알파벳 별 조이스틱 조작 횟수를 반복문과 min()함수를 이용해 계산한 예시이다.

```python
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d={}
for i in range(len(alpha)):
    d[alpha[i]]=min(i,26-i)
```

---

### 출처

문제 출처

[https://programmers.co.kr/learn/courses/30/lessons/42860](https://programmers.co.kr/learn/courses/30/lessons/42860)

참고 출처

[https://programmers.co.kr/learn/courses/30/lessons/42860/solution_groups?language=python3](https://programmers.co.kr/learn/courses/30/lessons/42860/solution_groups?language=python3)
