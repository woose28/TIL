const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, target] = data.map(Number);

const mat = new Array(N).fill(0).map(() => new Array(N).fill(0));
let targetPos = "1 1";

let cr = 0;
let cc = 0;

let dx = [0, 1, 0, -1];
let dy = [1, 0, -1, 0];

let cd = 0;

const startNumber = Math.pow(N, 2);

mat[0][0] = startNumber;

for (let i = startNumber - 1; i >= 1; i--) {
  let nr = cr + dy[cd];
  let nc = cc + dx[cd];

  if (0 > nr || nr >= N || 0 > nc || nc >= N || mat[nr][nc] !== 0) {
    cd = (cd + 1) % 4;

    nr = cr + dy[cd];
    nc = cc + dx[cd];
  }

  mat[nr][nc] = i;

  if (i === target) {
    targetPos = `${nr + 1} ${nc + 1}`;
  }

  cr = nr;
  cc = nc;
}

for (let row of mat) {
  console.log(row.join(" "));
}

console.log(targetPos);
