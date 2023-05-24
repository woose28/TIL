import sys

def solution(N, K):
  answer = []
  num_list = [ i for i in range(1, N + 1) ]
  
  k_count = 1
  current_index = 0

  while True:
    if k_count == K:
      answer.append(str(num_list[current_index]))
      del num_list[current_index]
      k_count = 0

      if len(num_list) == 0:
        break
      
      current_index = (current_index - 1) % len(num_list)
    
    else:
      k_count += 1
      current_index = (current_index + 1) % len(num_list)
  
    
  print(f"<{', '.join(answer)}>")


if __name__ == "__main__":
  N, K = map(int, sys.stdin.readline().strip().split(' '))

  solution(N, K)
