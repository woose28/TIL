# 시그널이 항성계 내에 무한히 전파될 수 있다며 Voyager를 출력한다.. 
# -> 시그널이 무한히 전파된다는 사실을 어떻게 알 수 있지?
# 시그널의 전파 시간이 N * M 보다 크면 무한히 전파?
# 블랙홀을 만나거나 항성계를 빠저나간 시간을 구해야하지

N, M = map(int, input().split(' '))

mat = [ input() for _ in range(N) ]

_sr, _sc = map(int, input().split(' '))
sr = _sr - 1
sc = _sc - 1

max_direction = "U"
max_time = 0

initial_directions = ["U", "R", "D", "L"]
direction_map = {
  "U": [0, -1],
  "R": [1, 0],
  "D": [0, 1],
  "L": [-1, 0],
}

infinity_time = N * M

def change_direction(current_direction, planet_direction):
  if planet_direction == "/":
    if current_direction == "U":
      return "R"
    
    elif current_direction == "R":
      return "U"
    
    elif current_direction == "D":
      return "L"

    elif current_direction == "L":
      return "D"
  
  if planet_direction == "\\":
    if current_direction == "U":
      return "L"
    
    elif current_direction == "R":
      return "D"
    
    elif current_direction == "D":
      return "R"

    elif current_direction == "L":
      return "U"
    

for initial_direction in initial_directions:
  cr, cc = sr, sc

  current_direction = initial_direction
  current_time = 0

  while True:
    dx, dy = direction_map[current_direction]

    cr = cr + dy
    cc = cc + dx
    current_time += 1

    if cr == sr and cc == sc and current_direction == initial_direction:
      max_direction = initial_direction
      max_time = float('inf')
      break

    if not (0 <= cr < N and 0 <= cc < M) or mat[cr][cc] == "C":
      if max_time < current_time:
        max_direction = initial_direction
        max_time = current_time
      break
    
    if mat[cr][cc] == '/':
      current_direction = change_direction(current_direction, "/")
      
    if mat[cr][cc] == '\\':
      current_direction = change_direction(current_direction, '\\')
      
  if max_time == float('inf'):
    break


print(max_direction)

if max_time == float("inf"):
  print('Voyager')
else:
  print(max_time)
