const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());

const paper = new Array(103).fill(0).map(() => new Array(103).fill(0));

data.forEach((position) => {
  const [x, y] = position.split(" ").map(Number);

  for (let i = x + 1; i < x + 11; i++) {
    for (let j = y + 1; j < y + 11; j++) {
      paper[i][j] = 1;
    }
  }
});

const visited = new Array(103).fill(0).map(() => new Array(103).fill(false));

let answer = 0;

const d = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

for (let i = 1; i < 102; i++) {
  for (let j = 1; j < 102; j++) {
    if (paper[i][j] === 0 || visited[i][j]) {
      continue;
    }

    const stack = [[i, j]];
    visited[i][j] = true;

    while (stack.length > 0) {
      const [cr, cc] = stack.pop();

      d.forEach(([dy, dx]) => {
        const nr = cr + dy;
        const nc = cc + dx;

        if (0 <= nr && nr < 102 && 0 <= nc && nc < 102) {
          if (paper[nr][nc] === 0) {
            answer += 1;
          } else if (paper[nr][nc] === 1 && !visited[nr][nc]) {
            visited[nr][nc] = true;
            stack.push([nr, nc]);
          }
        }
      });
    }
  }
}

console.log(answer);
