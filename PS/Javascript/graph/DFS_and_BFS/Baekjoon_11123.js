const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(data.shift());

const answers = [];

const d = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

for (let i = 0; i < T; i++) {
  const [H, W] = data.shift().split(" ").map(Number);

  const grid = [];

  for (let j = 0; j < H; j++) {
    grid.push(data.shift().split(""));
  }

  const visited = new Array(H).fill(0).map(() => new Array(W).fill(false));

  let groupCount = 0;

  for (let j = 0; j < H; j++) {
    for (let k = 0; k < W; k++) {
      if (grid[j][k] === "." || visited[j][k]) {
        continue;
      }

      visited[j][k] = true;
      groupCount += 1;

      const stack = [[j, k]];

      while (stack.length > 0) {
        const [cr, cc] = stack.pop();

        d.forEach(([dy, dx]) => {
          const nr = cr + dy;
          const nc = cc + dx;

          if (
            0 <= nr &&
            nr < H &&
            0 <= nc &&
            nc < W &&
            grid[nr][nc] === "#" &&
            !visited[nr][nc]
          ) {
            visited[nr][nc] = true;
            stack.push([nr, nc]);
          }
        });
      }
    }
  }

  answers.push(groupCount);
}

console.log(answers.join("\n"));
