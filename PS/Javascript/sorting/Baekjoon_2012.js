const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(data) {
  const [n, ...hopeRanks] = data.map(Number);

  const answer = hopeRanks
    .sort((a, b) => a - b)
    .reduce((acc, curRank, index) => acc + Math.abs(curRank - (index + 1)), 0);

  console.log(answer);
}

solution(data);
