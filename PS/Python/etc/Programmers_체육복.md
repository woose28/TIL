# Programmers_체육복

### **문제 설명**

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 전체 학생의 수는 2명 이상 30명 이하입니다.
- 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

### 입출력 예

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51f518a1-b0c1-46d7-94df-cb70f20eff04/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51f518a1-b0c1-46d7-94df-cb70f20eff04/Untitled.png)

### 입출력 예 설명

예제 #1

1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2

3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

---

### 풀이

이 문제는 lost에 있는 요소 마다 아래의 3가지 경우를 확인해서 체육복 대여 가능 여부를 판단하는게 핵심이라 생각한다.

- 경우 1 : lost의 i번째 요소가 reserve 리스트에 존재하는가?
- 경우 2 : lost의 i-1번째 요소가 reserve 리스트에 존재하는가?
- 경우 3 : lost의 i+1번쨰 요소가 reserve 리스트에 존재하는가?

단, 위의 3가지 조건만으로는 문제의 마지막 제한사항을 충족시키지 못하기 때문에 문제를 완전히 해결할 수 없다.

Ex 테스트 케이스)

테스트 케이스가 아래와 같이 주어진다.

- n = 5
- lots = [2,3]
- reserve = [3, 4]

위의 3가지 조건만으로 문제를 풀때 : answer = 5

그러나 문제의 제한사항에 의하면 여별읠 체육복을 소유한 학생이 도난을 당했을 때, 해당 학생은 다른 학생에게 체육복을 대여할 수 없다.

이 조건에 의한 결과 : answer = 4

따라서 마지막 제한사항을 충족 시키기 위해 lost와 reserve list에 동일한 요소가 존재할 경우 각 리스트에서 해당 요소를 삭제하는 기능을 구현해야 한다.

```python
def solution(n, lost, reserve):
    answer = n

    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    for i in lost:
        if i in reserve:
            reserve.remove(i)
            continue
        elif i-1 in reserve:
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            continue
        answer -= 1

    return answer
```

---

### 출처

- 문제 출처

    [https://programmers.co.kr/learn/courses/30/lessons/42862](https://programmers.co.kr/learn/courses/30/lessons/42862)
