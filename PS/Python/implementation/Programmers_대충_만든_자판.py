def solution(keymap, targets):
    answer = []
    
    alphabetCount = {}
    
    for key in keymap:
        for index, alphabet in enumerate(key):
            
            if alphabet in alphabetCount:
                if alphabetCount.get(alphabet) > index + 1:
                    alphabetCount[alphabet] = index + 1
    
            else:
                alphabetCount[alphabet] = index + 1
    
    
    for target in targets:
        count = 0
        isWritable = True
        
        for alphabet in target:
            if alphabet in alphabetCount:
                count += alphabetCount[alphabet]
            else:
                isWritable = False
        
        if isWritable:
            answer.append(count)
        else:
            answer.append(-1)
        
    return answer