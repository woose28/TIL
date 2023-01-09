const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = data[0].split(" ").map(Number);
const moves = data[1].split("");

let answer = 1;
let cr = 1,
  cc = 1;

let startNum = 1;

moves.forEach((move) => {
  if (move === "U") {
    cr -= 1;
  } else if (move === "D") {
    cr += 1;
  } else if (move === "R") {
    cc += 1;
  } else if (move === "L") {
    cc -= 1;
  }

  const diagonalNum = cr + cc;
  let target = 0;

  if (diagonalNum <= N + 1) {
    startNum +=
      move === "U" || move === "L" ? -(diagonalNum - 1) : diagonalNum - 2;
  } else if (diagonalNum > N + 1) {
    startNum +=
      move === "U" || move === "L"
        ? -(2 * N - (diagonalNum - 1))
        : 2 * N - (diagonalNum - 2);
  }

  if (diagonalNum % 2 === 0) {
    if (diagonalNum < N + 1) {
      target = startNum + (diagonalNum - 1) - cr;
    } else {
      target = startNum + (N - cr);
    }
  } else {
    if (diagonalNum > N + 1) {
      target = startNum + (cr - (diagonalNum - N));
    } else {
      target = startNum + cr - 1;
    }
  }

  answer += target;
});

console.log(answer);
