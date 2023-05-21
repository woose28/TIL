import sys

def solution(some_string, other_string):
  dp = [ [0] * (len(other_string) + 1) for _ in range(len(some_string) + 1) ]

  for i in range(len(some_string)):
    for j in range(len(other_string)):
      if some_string[i] == other_string[j]:
        dp[i + 1][j + 1] = dp[i][j] + 1
      
      else:
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
  
  print(dp[len(some_string)][len(other_string)])

if __name__ == "__main__":
  some_string = list(sys.stdin.readline().strip())
  other_string = list(sys.stdin.readline().strip())

  solution(some_string, other_string)
