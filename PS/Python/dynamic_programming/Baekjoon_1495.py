N, S, M = map(int, input().split(' '))
V = list(map(int, input().split(' ')))

def solution(N, S, M, V):
  answer = - 1
  prev_v_list = set([ S ])

  for i in range(N):
    cur_v = V[i]
    cur_v_list = set([])

    if len(prev_v_list) == 0:
      break

    for prev_v in prev_v_list:
      if prev_v - cur_v >= 0:
        cur_v_list.add(prev_v - cur_v)
      
      if prev_v + cur_v <= M:
        cur_v_list.add(prev_v + cur_v)
    
    prev_v_list = cur_v_list
  
  for v in prev_v_list:
    if v > answer:
      answer = v

  print(answer)

solution(N, S, M, V)
