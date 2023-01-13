const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

function solution(data) {
  const [T, ...NList] = data;

  const answerList = [];

  for (let i = 0; i < T; i++) {
    const N = NList[i];

    let left = 1;
    let right = N;

    while (left <= right) {
      const mid = Number.parseInt((left + right) / 2);

      const maxStoneCount =
        (1 + mid) * Number.parseInt(mid / 2) +
        (Number.parseInt(mid / 2) + 1) * (mid % 2);

      if (maxStoneCount > N) {
        right = mid - 1;
      } else if (maxStoneCount <= N) {
        left = mid + 1;
      }
    }

    answerList.push(right);
  }

  console.log(answerList.join("\n"));
}

solution(data);
