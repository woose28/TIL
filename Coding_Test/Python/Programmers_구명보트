# Programmers_구명보트

### **문제 설명**

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 **2명**씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

### 입출력 예

people = [70, 50, 80, 50] , limit = 100 : return = 3

people = [70, 80, 50], limit = 100 : return = 3

---

### 풀이

보트에 탈 수 있는 최대 인원은 2명이다.

따라서 가장 무거운 사람과 가장 가벼운 사람이 보트에 같이 탈 수 있는지 확인하는 것이 이 문제의 핵심이라 생각한다.

코드에서는 무거운 사람을 한명 씩 보트에 태우며 가벼운 사람과 같이 탈 수 있는지 확인하는 방법을 택했다.

```python
def solution(people, limit):
    answer = 0
    people.sort()

    light = 0
    heavy = len(people) - 1

    while(light <= heavy):
        answer+=1
        if(people[light] + people[heavy] <= limit):
            light += 1
        heavy -= 1

    return answer
```

★참고로 이 문제의 경우 리스트를 직접 조작(pop, remove) 등을 사용하면 시간초과가 나온다.

⇒ 자료구조를 직접 조작할 필요가 없는 문제라면 인덱스 만으로 해결하는 습관을 들여야 할 것 같다.

---

### 출처

문제 출처

[https://programmers.co.kr/learn/courses/30/lessons/42885](https://programmers.co.kr/learn/courses/30/lessons/42885)

참고 출처

[https://leedakyeong.tistory.com/entry/프로그래머스-구명보트-in-python](https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python)
