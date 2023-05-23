import sys

def solution(some_string, other_string):
  dp = [ [0] * (len(other_string) + 1) for _ in range(len(some_string) + 1) ]

  for i in range(len(some_string)):
    for j in range(len(other_string)):
      if some_string[i] == other_string[j]:
        dp[i + 1][j + 1] = dp[i][j] + 1
      
      else:
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
  
  lcs = ''
  
  start_row = len(some_string)

  cr, cc = len(some_string), len(other_string)

  while True:
    if dp[cr][cc] == 0:
      break
    
    elif dp[cr][cc] == dp[cr][cc - 1]:
      cc -= 1
    
    elif dp[cr][cc] == dp[cr - 1][cc]:
      cr -= 1
    
    else:
      lcs += some_string[cr - 1]
      cr -= 1
      cc -= 1


  print(dp[len(some_string)][len(other_string)])

  if len(lcs) > 0:
    print(lcs[::-1])
  

if __name__ == "__main__":
  some_string = list(sys.stdin.readline().strip())
  other_string = list(sys.stdin.readline().strip())

  solution(some_string, other_string)
