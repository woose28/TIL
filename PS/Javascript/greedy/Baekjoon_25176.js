const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const N = Number(fs.readFileSync(filePath).toString().trim());

let answer = 1;

for (let i = N; i > 0; i--) {
  answer *= i;
}

console.log(answer);
