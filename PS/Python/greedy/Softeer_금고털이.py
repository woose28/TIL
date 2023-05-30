import sys

def solution(W, N, jewels):
  answer = 0
  remain_weight = W

  for i in range(N):
    if remain_weight == 0:
      break
    
    cur_jewel_weight, cur_jewel_price = jewels[i]

    cur_using_weight = min(cur_jewel_weight, remain_weight)

    answer += cur_jewel_price * cur_using_weight
    remain_weight -= cur_using_weight

  print(answer)


if __name__ == "__main__":
  W, N = map(int, input().split(' '))
  jewels = [ list(map(int, input().split(' '))) for _ in range(N) ]

  jewels.sort(key = lambda x: (-x[1]))

  solution(W, N, jewels)
