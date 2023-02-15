const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, ..._mat] = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(_N);
const mat = _mat.map((row) => row.split(""));

let answer = [0, 0];

for (let i = 0; i < N; i++) {
  let continuousBlank = 0;

  for (let j = 0; j < N; j++) {
    if (mat[i][j] === "X") {
      continuousBlank = 0;
      continue;
    }

    continuousBlank += 1;

    if (continuousBlank === 2) {
      answer[0] += 1;
    }
  }
}

for (let i = 0; i < N; i++) {
  let continuousBlank = 0;

  for (let j = 0; j < N; j++) {
    if (mat[j][i] === "X") {
      continuousBlank = 0;
      continue;
    }

    continuousBlank += 1;

    if (continuousBlank === 2) {
      answer[1] += 1;
    }
  }
}

console.log(answer.join(" "));
