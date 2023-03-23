const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = data.shift().split(" ").map(Number);

if (N === 0) {
  console.log(0);
  return;
}

const bookWeights = data.pop().split(" ").map(Number);

let answer = 1;

bookWeights.reduce((currentBoxWeight, currentBookWeight) => {
  if (currentBoxWeight + currentBookWeight > M) {
    answer += 1;
    return currentBookWeight;
  }

  return currentBoxWeight + currentBookWeight;
});

console.log(answer);
