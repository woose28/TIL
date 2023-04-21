
width, height = [ int(char) for char in input().split(' ') ]

shopCount = int(input())

shops = [ [ int(char) for char in input().split(' ')] for _ in range(shopCount) ]
startDirection, startDistance = [ int(char) for char in input().split(' ') ]

def calculatePos(width, height, direction, pos):
  if direction == 1:
    return pos

  elif direction == 2:
    return width + height + (width - pos)
  
  elif direction == 3:
    return width * 2 + height + (height - pos)
  
  return width + pos


def solution(width, height, shops, startDirection, startDistance):
  totalLength = width * 2 + height * 2

  answer = 0
  startPos = calculatePos(width, height, startDirection, startDistance)

  for shopDirection, shopDistance in shops:
    shopPos = calculatePos(width, height, shopDirection, shopDistance)

    minPos = min(startPos, shopPos)
    maxPos = max(startPos, shopPos)

    answer += min(maxPos - minPos, totalLength - maxPos + minPos)

  print(answer)

solution(width, height, shops, startDirection, startDistance)
