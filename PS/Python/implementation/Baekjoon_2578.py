bingo_map = {}
bingo_mat = [ list(map(int, input().split(' '))) for _ in range(5) ]
speaking_number = []

for row_index, row in enumerate(bingo_mat):
  for column_index, bingo_num in enumerate(row):
    bingo_map[bingo_num] = [row_index, column_index]

for _ in range(5):
  speaking_number.extend(list(map(int, input().split(' '))))

def is_row_bingo(used_mat, cr):
  is_bingo = True
  
  for cc in range(5):
    if not used_mat[cr][cc]:
      is_bingo = False
      break
  
  return is_bingo

def is_column_bingo(used_mat, cc):
  is_bingo = True
  
  for cr in range(5):
    if not used_mat[cr][cc]:
      is_bingo = False
      break
  
  return is_bingo

def is_right_upper_cross_bingo(used_mat, cr, cc):
  is_bingo = True

  if cr + cc != 4:
    is_bingo = False

  else:
    for i in range(5):
      if not used_mat[i][4-i]:
        is_bingo = False
        break

  return is_bingo

def is_left_upper_cross_bingo(used_mat, cr, cc):
  is_bingo = True

  if cr != cc:
    is_bingo = False

  else:
    for i in range(5):
      if not used_mat[i][i]:
        is_bingo = False
        break

  return is_bingo

def solution(bingo_map, speaking_number):
  answer = 0
  bingo_line = 0

  used_mat = [ [False] * 5 for _ in range(5) ] 

  for speaking_order, current_number in enumerate(speaking_number):
    cr, cc = bingo_map[current_number]

    used_mat[cr][cc] = True

    if is_row_bingo(used_mat, cr):
      bingo_line += 1

    if is_column_bingo(used_mat, cc):
      bingo_line += 1

    if is_right_upper_cross_bingo(used_mat, cr, cc):
      bingo_line += 1

    if is_left_upper_cross_bingo(used_mat, cr, cc):
      bingo_line += 1

    if bingo_line >= 3:
      answer = speaking_order + 1
      break

  print(answer)

solution(bingo_map, speaking_number)
