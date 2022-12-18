function solution(maps) {
  var answer = -1;

  const n = maps.length;
  const m = maps[0].length;

  const visitied = new Array(n).fill(0).map(() => new Array(m).fill(false));
  visitied[0][0] = true;

  const dx = [0, 1, 0, -1];
  const dy = [-1, 0, 1, 0];

  const que = [[0, 0, 1]];

  while (que.length !== 0) {
    const [cx, cy, cc] = que.shift();

    for (let i = 0; i < 4; i++) {
      const nx = cx + dx[i];
      const ny = cy + dy[i];

      if (nx === m - 1 && ny === n - 1) {
        return cc + 1;
      }

      if (
        0 <= nx &&
        nx < m &&
        0 <= ny &&
        ny < n &&
        maps[ny][nx] === 1 &&
        !visitied[ny][nx]
      ) {
        visitied[ny][nx] = true;
        que.push([nx, ny, cc + 1]);
      }
    }
  }

  return answer;
}
