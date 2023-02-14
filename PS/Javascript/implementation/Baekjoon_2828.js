const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_NM, _J, ..._applePos] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = _NM.split(" ").map(Number);
const J = Number(_J);
const applePos = _applePos.map(Number);

let answer = 0;
let basketLeft = 1;

applePos.forEach((pos) => {
  const basketRight = basketLeft + M - 1;

  if (basketLeft <= pos && pos <= basketRight) {
    return;
  }

  if (basketLeft < pos) {
    answer += pos - basketRight;
    basketLeft = pos - (M - 1);
    return;
  }

  answer += basketLeft - pos;
  basketLeft = pos;
});

console.log(answer);
