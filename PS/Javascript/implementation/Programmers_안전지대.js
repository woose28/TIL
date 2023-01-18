function solution(board) {
  const n = board.length;
  let answer = n * n;

  const dx = [-1, 0, 1, 1, 1, 0, -1, -1];
  const dy = [-1, -1, -1, 0, 1, 1, 1, 0];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 1) {
        answer -= 1;

        for (let k = 0; k < 8; k++) {
          const ny = i + dy[k];
          const nx = j + dx[k];

          if (0 <= nx && nx < n && 0 <= ny && ny < n && board[ny][nx] === 0) {
            board[ny][nx] = 2;
            answer -= 1;
          }
        }
      }
    }
  }

  return answer;
}
