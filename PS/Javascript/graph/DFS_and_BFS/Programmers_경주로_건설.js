function solution(board) {
  var answer = 0;

  const N = board.length;
  const cost = new Array(N)
    .fill(0)
    .map((row) =>
      new Array(N).fill(0).map((cell) => new Array(2).fill(Infinity))
    );

  const costStraight = 100;
  const costCorner = 500;

  const dx = [0, 1, 0, -1];
  const dy = [-1, 0, 1, 0];

  const stack = [[0, 0, 0, -1]];

  while (stack.length) {
    const [cy, cx, cc, cd] = stack.pop();

    dx.forEach((x, index) => {
      const ny = cy + dy[index];
      const nx = cx + x;

      const nc =
        cc +
        costStraight +
        ((cd + index) % 2 === 1 && cd !== -1 ? costCorner : 0);

      if (
        0 <= ny &&
        ny < N &&
        0 <= nx &&
        nx < N &&
        board[ny][nx] === 0 &&
        cost[ny][nx][index % 2] >= nc
      ) {
        stack.push([ny, nx, nc, index]);
        cost[ny][nx][index % 2] = nc;
      }
    });
  }

  answer = Math.min(...cost[N - 1][N - 1]);

  return answer;
}
