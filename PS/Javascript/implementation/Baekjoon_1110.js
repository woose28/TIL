const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const number = Number(fs.readFileSync(filePath).toString().trim());

let answer = 0;

let cycleNumber = number;

while (true) {
  const newNumber = Number.parseInt(cycleNumber / 10) + (cycleNumber % 10);

  cycleNumber = (cycleNumber % 10) * 10 + (newNumber % 10);

  answer += 1;

  if (number === cycleNumber) {
    break;
  }
}

console.log(answer);
