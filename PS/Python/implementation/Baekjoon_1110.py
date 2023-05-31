import sys

if __name__ == "__main__":
  N = int(sys.stdin.readline().strip())
  new_number = N
  answer = 0

  while True:
    if new_number < 10:
      new_number = int(str(new_number) + str(new_number))

    elif new_number >= 10:
      string_number = str(new_number)
      
      sum_number = int(string_number[0]) + int(string_number[1])

      if sum_number < 10:
        new_number = int(string_number[1] + str(sum_number))
      
      elif sum_number >= 10:
        new_number = int(string_number[1] + str(sum_number)[1])

    answer += 1

    if new_number == N:
      break
  
  print(answer)
  