def solution(name, yearning, photo):
    answer = []
    
    yearningPerName = { n: y for n, y in zip(name,  yearning)}
    
    for p in photo:
        sumYearning = sum([yearningPerName[n] if n in yearningPerName else 0 for n in p ])
        
        answer.append(sumYearning)
    
    return answer