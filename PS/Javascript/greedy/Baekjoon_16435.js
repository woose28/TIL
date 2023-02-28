const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_NL, _fruits] = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, L] = _NL.split(" ").map(Number);
const fruits = _fruits.split(" ").map(Number);

fruits.sort((a, b) => a - b);

let answer = L;

fruits.every((fruit) => {
  if (answer < fruit) {
    return false;
  }

  answer += 1;

  return true;
});

console.log(answer);
