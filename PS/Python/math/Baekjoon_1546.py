import sys

def solution(N, score_list):
  answer = 0

  max_score = max(score_list)

  new_score_list = [ (score / max_score) * 100 for score in score_list ]

  answer = sum(new_score_list) / N

  print(answer)

if __name__ == "__main__":
  N = int(sys.stdin.readline())
  score_list = list(map(int, sys.stdin.readline().split(' ')))

  solution(N, score_list)
