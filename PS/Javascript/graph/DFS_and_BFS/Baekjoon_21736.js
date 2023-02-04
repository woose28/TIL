const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [NM, ...mat] = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, M] = NM.split(" ").map(Number);

const campus = new Array(N).fill(0).map(() => new Array(M).fill(0));
const visited = new Array(N).fill(0).map(() => new Array(M).fill(false));

let sr = 0;
let sc = 0;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (mat[i][j] === "I") {
      sr = i;
      sc = j;
    }

    campus[i][j] = mat[i][j];
  }
}

const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

const stack = [[sr, sc]];
visited[sr][sc] = true;

let answer = 0;

while (stack.length !== 0) {
  const [cr, cc] = stack.pop();

  dx.forEach((directionX, index) => {
    const nr = cr + dy[index];
    const nc = cc + directionX;

    if (
      nr >= 0 &&
      nr < N &&
      nc >= 0 &&
      nc < M &&
      campus[nr][nc] !== "X" &&
      !visited[nr][nc]
    ) {
      visited[nr][nc] = true;

      if (campus[nr][nc] === "P") {
        answer += 1;
      }

      stack.push([nr, nc]);
    }
  });
}

console.log(answer || "TT");
