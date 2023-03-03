const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data[0]);
const numbers = data[1].split(" ").map(Number);
const M = Number(data[2]);

const isPalindrome = new Array(N).fill(0).map(() => new Array(N).fill(0));

for (let i = 0; i < N; i++) {
  isPalindrome[i][i] = 1;
}

for (let i = 0; i < N - 1; i++) {
  if (numbers[i] === numbers[i + 1]) {
    isPalindrome[i][i + 1] = 1;
  }
}

for (let i = 2; i < N; i++) {
  for (let j = 0; j < N - i; j++) {
    if (numbers[j] === numbers[j + i] && isPalindrome[j + 1][j + i - 1] === 1) {
      isPalindrome[j][j + i] = 1;
    }
  }
}

const answer = [];

for (let i = 0; i < M; i++) {
  const [S, E] = data[i + 3].split(" ").map(Number);

  answer.push(isPalindrome[S - 1][E - 1]);
}

console.log(answer.join("\n"));
