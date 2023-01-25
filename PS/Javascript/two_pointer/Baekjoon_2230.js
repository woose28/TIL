const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = data[0].split(" ").map(Number);

const numList = data.slice(1).map(Number);
numList.sort((a, b) => a - b);

let answer = Infinity;

let start = 0;
let end = 0;

while (end < N) {
  const diff = numList[end] - numList[start];

  if (diff >= M) {
    if (answer > diff) {
      answer = diff;
    }

    start += 1;
    continue;
  }

  end += 1;
}

console.log(answer);
