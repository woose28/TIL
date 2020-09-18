### 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

### 입출력 예

brown = 3, yellow = 2 : return = [4, 3]

brown = 8, yellow = 1 : return = [3, 3]

brown = 24, yellow = 24 : return = [8, 6]

---

### 나의 풀이

이 문제는 카펫의 가로와 세로의 길이를 구하는 문제이다.

따라서 먼저 조건(총 격자 수)에 맞는 가로, 세로의 경우의 수를 구하는 것이 우선이라 생각했다.

조건은 다음과 같다.

총 격자 수 = (카펫의 가로 길이) * (카펫의 세로 길이)

조건을 통해 가로와 세로의 길이는 총 격자 수의 약수라는 것을 알게 되었고 경우의 수를 줄였다.

약수들의 쌍에서 정답을 찾기 위해 노란색 격자의 수를 이용했다.

갈색 격자는 카펫의 테두리에 배치되므로 다음과 같은 조건을 생각할 수 있다.

노란색 격자의 수 = (가로의 길이 -2 ) * (세로의 길이 -2)

마지막으로 '가로의 길이 ≥ 세로의 길이'인 제한 조건을 따르면 문제는 해결 된다.

```python
def solution(brown, yellow):
    answer = []

    total = brown+yellow

    for height in range(2, total//2):
        if(total % height == 0):
            width = total / height
            if(yellow == total - 2*width - 2*height + 4 and width >= height):
                answer.extend([width, height])


    return answer
```

---

### 다른 풀이

근의 공식, 둘레를 이용한 방법 등이 있다.
