const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [paperCount, ...papers] = data;

const whitePaper = new Array(100).fill(0).map(() => new Array(100).fill(true));
let answer = 0;

papers.forEach((paper) => {
  const [startColumn, startRow] = paper.split(" ").map(Number);

  for (let i = startColumn - 1; i < startColumn + 9; i++) {
    for (let j = startRow - 1; j < startRow + 9; j++) {
      if (whitePaper[j][i]) {
        whitePaper[j][i] = false;
        answer += 1;
      }
    }
  }
});

console.log(answer);
