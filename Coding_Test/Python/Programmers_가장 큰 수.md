#Programmers_가장 큰 수

### **문제 설명**

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

### 입출력 예

numbers = [6, 10, 2] : return = "6210"

numbers = [3, 30, 34, 5, 9] : return = "9534330"

---

### 풀이

이 문제는 문자열을 정렬하는 기준을 찾는 것이 핵심이라 생각했다.

문자열을 순서대로 정렬한 후 3과 30 같은 관계를 정답에 맞게 정렬하기 위해 조건을 생각하여 시도했지만 결국 실패하였다.

다른 사람의 코드를 참고하니 정렬 아래와 같은 정렬 기준을 알 수 있었다.

```
i, j = 인접한 문자

if(i + j >j +i):
	i가 j보다 우선순위가 높다.
else:
	j가 i보다 우선순위가 높다.

#예시
i = "3"
j = "30"

i + j = "330"
j + i = "303"

으로 "3"이 "30"보다 우선순위가 높다.
```

위 기준을 삽입정렬에 적용하여 문제를 해결하였다.

```python
def solution(numbers):
    answer = ''
    str_num = list(map(str, numbers))
    str_num.sort()

    for i in range(1, len(str_num)):
        for j in range(i, 0, -1):
            if(str_num[j]+str_num[j-1] < str_num[j-1]+str_num[j]):
                str_num[j], str_num[j-1] = str_num[j-1], str_num[j]
            else:
                break

    str_num.reverse()

    answer = str(int("".join(str_num)))
    return answer
```

---

### 다른 풀이

가장 큰 수의 첫번째 풀이

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
```

-박상희님의 설명

문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.

---

### 출처

문제 출처

[https://programmers.co.kr/learn/courses/30/lessons/42746](https://programmers.co.kr/learn/courses/30/lessons/42746)

참고 출처

[https://eda-ai-lab.tistory.com/467](https://eda-ai-lab.tistory.com/467)
