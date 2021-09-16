def convertToNum(time):
    h, m, s = map(int, time.split(":"))
    
    return h * 3600 + m * 60 + s
    
def convertToStr(time):
    h = "0"+str(time // 3600) if time // 3600 < 10 else str(time // 3600)
    m = "0"+str((time % 3600) // 60) if (time % 3600) // 60 < 10 else str((time % 3600) // 60)
    s = "0"+str((time % 3600) % 60) if (time % 3600) % 60 < 10 else str((time % 3600) % 60)
    
    return h+":"+m+":"+s
    

def solution(play_time, adv_time, logs):
    pt, at = convertToNum(play_time), convertToNum(adv_time)
    
    total_time = [0] * (pt + 1)
    
    answer = 0
    
    for log in logs:
        st, et = log.split("-")
        st, et = convertToNum(st), convertToNum(et)
        
        total_time[st] += 1
        total_time[et] -= 1
        
        
    for idx in range(1, pt+1):
        total_time[idx] = total_time[idx] + total_time[idx-1]
        
    for idx in range(1, pt+1):
        total_time[idx] = total_time[idx] + total_time[idx-1]
    
    max_time = total_time[at-1]
    
    for i in range(at, pt):
            
        cur_time = total_time[i] - total_time[i-at]
        if max_time < cur_time:
            max_time = cur_time
            answer = i - at + 1
        

    answer = convertToStr(answer)
                
    return answer