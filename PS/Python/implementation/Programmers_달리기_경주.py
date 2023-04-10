def solution(players, callings):
    answer = []
    
    rank = { player: index for index, player in enumerate(players) }
    
    for call in callings:
        calledIndex = rank[call];
        
        frontPlayer = players[calledIndex - 1]
        
        players[calledIndex] = frontPlayer;
        players[calledIndex - 1] = call;
        
        rank[frontPlayer] = calledIndex;
        rank[call] = calledIndex - 1
        
    answer = players
    
    return answer