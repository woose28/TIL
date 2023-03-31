const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = data.shift().split(" ").map(Number);

const mat = new Array(N).fill(0).map(() => new Array(M).fill("."));

data.forEach((position) => {
  const [r, c] = position.split(" ").map(Number);

  mat[r - 1][c - 1] = "#";
});

let answer = 0;

const d = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (mat[i][j] !== "#") {
      continue;
    }

    let foodSize = 1;
    const stack = [[i, j]];
    mat[i][j] = "/";

    while (stack.length > 0) {
      const [cr, cc] = stack.pop();

      d.forEach(([dy, dx]) => {
        const nr = cr + dy;
        const nc = cc + dx;

        if (0 <= nr && nr < N && 0 <= nc && nc < M && mat[nr][nc] === "#") {
          mat[nr][nc] = "/";
          foodSize += 1;
          stack.push([nr, nc]);
        }
      });
    }

    answer = Math.max(answer, foodSize);
  }
}

console.log(answer);
