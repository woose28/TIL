import sys

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split(' ')))

left = 0
right = N - 1

minCharacteristicValue = float('inf')
answer = []

while left < right:
  sumLiquidValue = liquid[left] + liquid[right]
  currentCharacteristicValue = abs(sumLiquidValue)

  if currentCharacteristicValue < minCharacteristicValue:
    minCharacteristicValue = currentCharacteristicValue
    answer = [liquid[left], liquid[right]]

  if sumLiquidValue == 0:
    break

  elif sumLiquidValue > 0:
    right -= 1
  
  elif sumLiquidValue < 0:
    left += 1
  
print(' '.join(map(str, answer)))
