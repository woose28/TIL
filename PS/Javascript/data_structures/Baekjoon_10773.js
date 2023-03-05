const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [K, ...numbers] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const stack = [];

numbers.forEach((number) => {
  if (number === 0) {
    stack.pop();
    return;
  }

  stack.push(number);
});

const answer = stack.reduce((acc, number) => acc + number, 0);

console.log(answer);
