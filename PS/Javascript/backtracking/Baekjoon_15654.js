const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [NM, stringNumbers] = data;

const [N, M] = NM.split(" ").map(Number);
const numbers = stringNumbers.split(" ").map(Number);

numbers.sort((a, b) => a - b);

const answer = [];
const isUsed = new Array(N).fill(false);

function solution(selected) {
  if (selected.length === M) {
    answer.push(selected.join(" "));
  }

  numbers.forEach((number, index) => {
    if (!isUsed[index]) {
      isUsed[index] = true;
      solution([...selected, number]);
      isUsed[index] = false;
    }
  });
}

solution([]);

console.log(answer.join("\n"));
