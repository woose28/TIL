const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [N, ...tips] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

tips.sort((a, b) => b - a);

const answer = tips.reduce(
  (acc, tip, index) => acc + Math.max(0, tip - index),
  0
);

console.log(answer);
