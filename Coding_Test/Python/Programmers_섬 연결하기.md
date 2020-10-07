# Programmers_섬 연결하기

### **문제 설명**

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

### 제한사항

- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 `((n-1) * n) / 2`이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

### 입출력 예

n = 4, costs = [[0,1,1], [0,2,2], [1,2,5], [1,3,1], [2,3,8]] : return = 4

### 입출력 예 설명

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fb14bac-dc61-4ea9-95bd-c56a8a77fd1f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fb14bac-dc61-4ea9-95bd-c56a8a77fd1f/Untitled.png)

---

### 풀이

이 문제는 최소 신장 트리를 구현하는 문제라 생각된다.

따라서 비용을 기준으로 정렬한 후 사이클이 생기지 않도록 각 노드를 순회하면 된다.

이는 최소 신장 트리를 구현하는 것과 같으며

최소 신장 트리를 구현하는 알고리즘 중 하나인 Kruskal(크루스칼)알고리즘을 이용하면 이 문제를 해결 할 수 있다.

```python
def solution(n, costs):
    def find(vertex):
        if(root[vertex] != vertex):
            root[vertex] = find(root[vertex])
        return root[vertex]

    def union(root_01, root_02):
        if(rank[root_01] > rank[root_02]):
            root[root_02] = root_01
        else:
            root[root_01] = root_02
            if(root_01 == root_02):
                rank[root_02] += 1

    answer = 0

    root = {}
    rank = {}

    for i in range(n):
        root[i] = i
        rank[i] = 0

    costs.sort(key=lambda x : x[2])

    for cost in costs:
        root_01 = find(cost[0])
        root_02 = find(cost[1])

        if(root_01 != root_02):
            union(root_01, root_02)
            answer += cost[2]


    return answer
```

---

### 출처

문제출처

[https://programmers.co.kr/learn/courses/30/lessons/42861](https://programmers.co.kr/learn/courses/30/lessons/42861)
