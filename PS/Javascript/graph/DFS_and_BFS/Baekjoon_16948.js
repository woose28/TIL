const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());

const [r1, c1, r2, c2] = data[0].split(" ").map(Number);

const visited = new Array(N).fill(false).map(() => new Array(N).fill(false));

const d = [
  [-2, -1],
  [-2, 1],
  [0, -2],
  [0, 2],
  [2, -1],
  [2, 1],
];
const queue = [[r1, c1, 0]];

visited[r1][c1] = true;

let answer = -1;

while (queue.length > 0) {
  const [cr, cc, cm] = queue.shift();

  if (cr === r2 && cc === c2) {
    answer = cm;
    break;
  }

  d.forEach(([dy, dx]) => {
    const nr = cr + dy;
    const nc = cc + dx;

    if (0 <= nr && nr < N && 0 <= nc && nc < N && !visited[nr][nc]) {
      visited[nr][nc] = true;
      queue.push([nr, nc, cm + 1]);
    }
  });
}

console.log(answer);
