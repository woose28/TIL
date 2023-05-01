def solution(t, p):
    answer = 0
    
    p_length = len(p)
    max_index = len(t) - len(p)

    for start_index in range(max_index + 1):
        part_t = t[start_index: start_index + p_length]
        
        if part_t <= p:
            answer += 1
    
    return answer