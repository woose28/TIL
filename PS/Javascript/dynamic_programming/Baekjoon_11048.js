const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(data) {
  const [size, ...stringMat] = data;
  const [N, M] = size.split(" ").map(Number);
  const mat = stringMat.map((stringData) => stringData.split(" ").map(Number));
  const dp = Array(N + 1)
    .fill(null)
    .map(() => Array(M + 1).fill(0));

  dp.forEach((row, ri) => {
    if (ri === 0) {
      return;
    }

    row.forEach((cc, ci) => {
      if (ci === 0) {
        return;
      }

      dp[ri][ci] =
        mat[ri - 1][ci - 1] + Math.max(dp[ri - 1][ci], dp[ri][ci - 1]);
    });
  });

  const answer = dp[N][M];
  console.log(answer);
}

solution(data);
