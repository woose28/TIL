const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const N = Number(fs.readFileSync(filePath).toString().trim());

const isWinCY = new Array(1001);

isWinCY[1] = true;
isWinCY[2] = false;
isWinCY[3] = true;
isWinCY[4] = false;

for (let i = 5; i <= 1001; i++) {
  isWinCY[i] = true;

  if (isWinCY[i - 1] || isWinCY[i - 3] || isWinCY[i - 4]) {
    isWinCY[i] = false;
  }
}

const answer = isWinCY[N] ? "CY" : "SK";

console.log(answer);
