const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const data = fs.readFileSync(filePath).toString().trim();

const [N, M] = data.split(" ").map(Number);

const answer = [];

function solution(selected, prevNum) {
  if (selected.length === M) {
    answer.push(selected.join(" "));
    return;
  }

  for (let i = prevNum; i <= N; i++) {
    solution([...selected, i], i);
  }
}

solution([], 1);

console.log(answer.join("\n"));
