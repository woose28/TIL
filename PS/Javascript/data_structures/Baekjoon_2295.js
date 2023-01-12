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
  const [N, ...U1] = data;
  let answer = 0;
  const U2 = new Set([]);

  U1.forEach((e1) => {
    U1.forEach((e2) => {
      U2.add(e1 + e2);
    });
  });

  for (const e1 of U1) {
    for (const e2 of U1) {
      if (e1 - e2 < 0) {
        continue;
      }

      if (U2.has(e1 - e2)) {
        answer = Math.max(answer, e1);
      }
    }
  }

  console.log(answer);
}

solution(data);
