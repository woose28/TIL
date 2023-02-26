def solution(s, skip, index):
    answer = ''
    
    skipList = [ ord(char) - 97 for char in skip ]
    
    for char in s:
        moveCount = 0
        currentChar = ord(char) - 97
        
        while moveCount < index:
            newChar = (currentChar + 1) % 26
            
            if not newChar in skipList:
                moveCount += 1
            currentChar = newChar
            
        
        answer += chr(currentChar + 97)
            
    return answer