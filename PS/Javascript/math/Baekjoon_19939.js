const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [N, K] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const minBallCount = K + (K * (K - 1)) / 2;

if (N < minBallCount) {
  console.log(-1);
  return;
}

if ((N - minBallCount) % K === 0) {
  console.log(K - 1);
  return;
}

console.log(K);
