#Permutations

**재귀를 통한 구현**

```python
#직접 구현 해보기
def permutation(data, r):
    used = [0] * len(data)
    
    def generate(chosen, used):
        if(len(chosen) == r):
            print(chosen)
            return

        for i in range(len(data)):
            if(used[i] == 0):
                chosen.append(data[i])
                used[i] = 1
                generate(chosen, used)
                chosen.pop()
                used[i] = 0
    generate([], used)

permutation([1, 2, 3, 4], 2)
```

1. 순열은 수의 순서도 고려하므로 (1, 2)와 (2, 1)은 다른 경우이다.

    ⇒ 때문에 반복문의 범위는 0 ~ len(data)까지이며

    이미 사용된 원소인지 파악하기 위해 used 리스트가 사용된다.

2. 재귀 함수의 리턴 조건은 '선택된 원소의 길이 == 사용자가 지정한 r' 이다.

### Itertools 이용

```python
import itertools

data = [1, 2, 3, 4]

print(list(itertools.permutations(data, 2)))
```

재귀로 구현한 코드와 동일한 결과를 반환하는 코드이다.

---

### 참고자료

- [https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations)
- [https://programmers.co.kr/learn/courses/4008/lessons/12836](https://programmers.co.kr/learn/courses/4008/lessons/12836)
