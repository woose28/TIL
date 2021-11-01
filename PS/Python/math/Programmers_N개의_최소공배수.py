def solution(arr):
    answer = 0
    
    cur_num = max(arr)
    
    while True:
        cnt = 0
        
        for num in arr:
            if cur_num % num != 0:
                break
            
            cnt += 1
            
        if cnt == len(arr):
            answer = cur_num
            break
        
        cur_num += 1
                
    return answer