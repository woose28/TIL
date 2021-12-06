'''
    제출 언어: Python3
    시간: 72ms
'''
import sys
import heapq

if __name__ == "__main__":
    N, D = map(int, sys.stdin.readline().strip().split())

    graph = {}
    adj_graph = {}

    node_list = []
    for _ in range(N):
        s, e, d = map(int, sys.stdin.readline().strip().split())
        node_list.extend([s, e])

        if e - s < d:
            d = e - s

        if s not in graph:
            graph[s] = [(e, d)]
        else:
            graph[s].append((e, d))
    
    node_list.append(0)
    node_list.append(D)

    node_list = list(set(node_list))
    node_list.sort()

    cnt_node = len(node_list)

    mat = [ [float('inf')] * cnt_node for _ in range(cnt_node) ]

    for i in range(cnt_node):
        cur_node = node_list[i]

        for j in range(i+1, cnt_node):
            next_node = node_list[j]
            mat[i][j] = next_node - cur_node

    for key, values in graph.items():
        cur_idx = node_list.index(key)

        for e, d in values:
            next_idx = node_list.index(e)

            if mat[cur_idx][next_idx] > d:
                mat[cur_idx][next_idx] = d

    adj_mat = [ [] for _ in range(cnt_node)]

    for i in range(cnt_node):
        for j in range(cnt_node):
            if mat[i][j] != float('inf'):
                adj_mat[i].append((mat[i][j], j))
    
    d = [ float('inf') ] * cnt_node
    d[0] = 0

    que = [ (0, 0) ]

    while que:
        cw, cn = heapq.heappop(que)

        if cw > d[cn]:
            continue
            
        for w, nn in adj_mat[cn]:
            nw = cw + w

            if nw < d[nn]:
                d[nn] = nw
                heapq.heappush(que, (nw, nn))
            
    d_idx = node_list.index(D)

    answer = d[d_idx]

    print(answer)

