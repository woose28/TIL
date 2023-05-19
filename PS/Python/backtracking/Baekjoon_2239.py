import sys
import copy

def solution(mat):
  zero_count = 0
  answer = None

  num_list = set([ str(i) for i in range(1, 10) ])

  def fill_square(cur_zero_count):
    nonlocal mat, answer
    
    if cur_zero_count == 0:
      answer = []

      for row in mat:
        answer.append(row[:])
      
      return
    
    cr = -1
    cc = -1

    for r in range(9):
      for c in range(9):
        if mat[r][c] == '0':
          cr = r
          cc = c
          break
        
      if cr != -1 and cc != -1:
        break

    row_enable_numbers = num_list - set(mat[cr])
    
    col_enable_numbers = num_list - set([ row[cc] for row in mat ])
    
    segment_enable_numbers_list = []

    for row in mat[3 * (cr // 3): 3 * (cr // 3) + 3]:
      for value in row[3 * (cc // 3): 3 * (cc // 3) + 3]:
        segment_enable_numbers_list.append(value)

    segment_enable_numbers = num_list - set(segment_enable_numbers_list)

    enable_numbers = list(row_enable_numbers & col_enable_numbers & segment_enable_numbers)
    enable_numbers.sort()

    for enable_number in enable_numbers:
      if answer is not None:
        break
      
      mat[cr][cc] = enable_number
      fill_square(cur_zero_count - 1)
      mat[cr][cc] = '0'
    
  for row in mat:
    for value in row:
      if value == '0':
        zero_count += 1

  fill_square(zero_count)

  for row in answer:
    print("".join(row))
  
if __name__ == "__main__":
  mat = [ list(sys.stdin.readline().strip()) for _ in range(9) ]

  solution(mat)
