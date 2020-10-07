# kruskal

### 설명

크루스칼 알고리즘은 그래프의 모든 점을 순회하는 최소 가중치(비용)을 구하는데 사용하는 알고리즘이다. 즉 **최소 신장 트리**를 만드는 알고리즘이다.

*크루스칼 알고리즘은 그리디 알고리즘에 기초한다.

### 예시 코드

```python
def find(vertex):
    if(root[vertex] != vertex):
        root[vertex] = find(root[vertex])
    return root[vertex]

def union(root_01, root_02):
    if(rank[root_01] > rank[root_02]):
        root[root_02] = root_01
    else:
        root[root_01] = root_02
        if(rank[root_01] == rank[root_02]):
            rank[root_02] += 1

root = {}
rank = {}

n = 8
costs = [[1,2,1], [1,5,7], [2,3,4], [3,5,2], [3,4,8], [4,5,2], [6,5,5], [6,7,3], [8,7,100]]

costs.sort(key= lambda x : x[2])

min_cost = 0
path = []

for i in range(n):
    root[i+1] = i+1
    rank[i+1] = 0

for cost in costs:
    root_01 = find(cost[0])
    root_02 = find(cost[1])

    if(root_01 != root_02):
        union(root_01, root_02)
        min_cost += cost[2]
        path.append(cost)    

print(min_cost)
```

1. 주어진 데이터를 가중치(비용)가 낮은 순으로 정렬한다.
2. find함수는 각 정점의 root를 찾아주는 함수이다
3. union함수는 두 정점의 root가 다를 때 호출되며 두 root를 하나로 통합하는 함수이다.
4. 입력 데이터를 순회하며 각각의 정점의 root가 다르다면 두 정점의 간선에 대한 가중치(비용)을 min_cost에 더한다.(union 과정으로 root를 하나로 통합)

---

### 출처

참고자료

[https://www.fun-coding.org/Chapter20-kruskal-live.html](https://www.fun-coding.org/Chapter20-kruskal-live.html)

[https://brownbears.tistory.com/461](https://brownbears.tistory.com/461)
