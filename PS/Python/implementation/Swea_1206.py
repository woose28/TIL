if __name__ == "__main__":
  for i in range(1, 11):
    N = int(input().strip())
    buildings = list(map(int, input().strip().split(' ')))
    
    answer = 0

    for j in range(N):
      near_highest_building = max(*buildings[j - 2: j], *buildings[j + 1: j + 3])
      
      if buildings[j] > near_highest_building:
        answer += buildings[j] - near_highest_building
    
    print(f'#{i} {answer}')