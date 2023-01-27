const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const data = fs.readFileSync(filePath).toString().trim();

const [N, M] = data.split(" ").map(Number);

const answer = [];

function solution(selected) {
  if (selected.length === M) {
    answer.push(selected.join(" "));
    return;
  }

  for (let i = 1; i <= N; i++) {
    solution([...selected, i]);
  }
}

solution([]);

console.log(answer.join("\n"));
