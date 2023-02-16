const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_NM, ..._papers] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = _NM.split(" ").map(Number);

const papers = _papers.map((row) => row.split(" ").map(Number));

const painting = new Array(100).fill(0).map(() => new Array(100).fill(0));

let answer = 0;

papers.forEach(([x1, y1, x2, y2]) => {
  for (let i = x1 - 1; i < x2; i++) {
    for (let j = y1 - 1; j < y2; j++) {
      painting[i][j] += 1;
    }
  }
});

painting.forEach((row) => {
  row.forEach((paperCount) => {
    if (paperCount > M) {
      answer += 1;
    }
  });
});

console.log(answer);
