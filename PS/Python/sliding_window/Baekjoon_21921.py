N, X  = map(int, input().split(' '))
visitor_cnt = list(map(int, input().split(' ')))

def solution(N, X, visitor_cnt):
  max_visitor_cnt = 0
  max_visitor_day_cnt = 0

  max_index = N - X

  cur_visitor_cnt = 0

  for start_index in range(max_index + 1):
    if start_index == 0:
      cur_visitor_cnt = sum(visitor_cnt[start_index: start_index + X])
    
    else:
      cur_visitor_cnt -= visitor_cnt[start_index - 1]
      cur_visitor_cnt += visitor_cnt[start_index + X - 1]
  
    if max_visitor_cnt < cur_visitor_cnt:
      max_visitor_cnt = cur_visitor_cnt
      max_visitor_day_cnt = 1
    
    elif max_visitor_cnt == cur_visitor_cnt:
      max_visitor_day_cnt += 1


  if max_visitor_cnt == 0:
    print("SAD")
  
  else:
    print(max_visitor_cnt)
    print(max_visitor_day_cnt)

solution(N, X, visitor_cnt)
