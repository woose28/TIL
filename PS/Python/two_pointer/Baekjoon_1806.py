import sys

N, S = map(int, sys.stdin.readline().split(' '))
numbers = list(map(int, sys.stdin.readline().split(' ')))

def solution(N, S, numbers):
  answer = float('inf')

  left_index = 0
  acc_number = 0

  for right_index in range(N):
    acc_number += numbers[right_index]

    if acc_number < S:
      continue
    
    if answer > right_index - left_index + 1:
      answer = right_index - left_index + 1

    while left_index <= right_index:
      acc_number -= numbers[left_index]
      left_index += 1

      if acc_number < S:
        break

      if answer > right_index - left_index + 1:
        answer = right_index - left_index + 1
      
    
      
  if answer == float('inf'):
    answer = 0

  print(answer)
  

solution(N, S, numbers)
