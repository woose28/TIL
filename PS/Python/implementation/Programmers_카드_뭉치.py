def solution(cards1, cards2, goal):
    answer = 'Yes'
        
    idxCards1 = 0
    idxCards2 = 0

    for word in goal:
        wordCard1 = cards1[idxCards1]
        wordCard2 = cards2[idxCards2]
        
        if wordCard1 == word:
            idxCards1 = min(idxCards1 + 1, len(cards1) - 1)
            continue
            
        elif wordCard2 == word:
            idxCards2 = min(idxCards2+ 1, len(cards2) - 1)
            continue
            
        answer = "No"
        break
    
    return answer