const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = data.shift().split(" ").map(Number);

const table = data.shift().split("");

let answer = 0;

for (let i = 0; i < N; i++) {
  if (table[i] !== "P") {
    continue;
  }

  const eatableStart = Math.max(0, i - K);
  const eatableEnd = Math.min(N - 1, i + K);

  for (let j = eatableStart; j <= eatableEnd; j++) {
    if (table[j] === "H") {
      table[j] = "B";
      answer += 1;
      break;
    }
  }
}

console.log(answer);
