const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

let charge = Number(fs.readFileSync(filePath).toString().trim());

let answer = 0;

let fiveCoinCount = Number.parseInt(charge / 5);

while (fiveCoinCount !== 0) {
  if ((charge - fiveCoinCount * 5) % 2 === 0) {
    answer += fiveCoinCount;
    charge -= fiveCoinCount * 5;
    break;
  }

  fiveCoinCount -= 1;
}

let twoCoinCount = Number.parseInt(charge / 2);

answer += twoCoinCount;
charge -= twoCoinCount * 2;

if (charge !== 0) {
  console.log(-1);
  return;
}

console.log(answer);
