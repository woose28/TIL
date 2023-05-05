S, K = map(int, input().split(' '))

def solution(S, K):
  answer = 1

  share = S // K
  remainder = S % K

  numbers = [share] * K
  cur_idx = 0

  while remainder > 0:
    numbers[cur_idx] += 1
    cur_idx = (cur_idx + 1) % len(numbers)
    remainder -= 1

  for number in numbers:
    answer *= number

  print(answer)

solution(S, K)
