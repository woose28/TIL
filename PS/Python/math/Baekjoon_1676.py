N = int(input())

factorial = 1

for i in range(1, N+1):
  factorial *= i

string_factorial = str(factorial)
answer = 0

for char in reversed(string_factorial):
  if char != '0':
    break
  
  answer += 1

print(answer)
