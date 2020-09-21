# Programmers_소수 찾기

### **문제 설명**

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

### 입출력 예

numbers = "17" : return = 3

numbers = "011" : return = 2

### 입출력 예 설명

예제 #1[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

- 11과 011은 같은 숫자로 취급합니다.

---

### 풀이

이 문제는

1. 만들 수 있는 모든 수 찾기
2. 1. 에서 찾은 숫자를 하나씩 확인하면 소수 찾기

위 두가지 부분으로 나뉜다고 생각했다.

1.은 permutation을 이용하여 구했으며 2. 는 직접 나누기를 해보며 진행했다.

```python
from itertools import permutations
def solution(numbers):
    answer = 0

    all_kind = []

    for i in range(len(numbers)):
        all_kind.extend(list(map(int, map("".join,permutations([i for i in numbers], i+1)))))

    all_kind = list(set(all_kind))

    for number in all_kind:
        flag = 0
        if(number < 2):
            continue
        for i in range(2, number // 2 + 1):
            if(number % i == 0):
                flag = 1
                break
        if(flag == 0):
            answer += 1

    return answer
```

*주의 사항

소수와 관련된 문제를 풀 때 2도 소수임을 꼭 기억하라!

(이걸 깜빡해서 1시간을 고생했다....ㅎㅎ)

---

### 참고 사항

소수를 구하는 방법은 직접 나눠서 구하는 방법 이외에 '에라토스테네스의 체'라는 것이 있다.

'에라토스테네스의 체'는 주어진 수까지의 모든 소수를 구하는 방법으로

이 문제에 어떻게 적용할지는 생각을 해봐야겠지만 코드는 아래와 같다.

```python
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```

---

### 출처

문제 출처

[https://programmers.co.kr/learn/courses/30/lessons/42839](https://programmers.co.kr/learn/courses/30/lessons/42839)

참고 출처

[https://ko.wikipedia.org/wiki/에라토스테네스의_체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
