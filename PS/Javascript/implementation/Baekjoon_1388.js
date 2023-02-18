const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_NM, ..._floor] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = _NM.split(" ").map(Number);
const floor = _floor.map((row) => row.split(""));

let answer = 0;

for (let i = 0; i < N; i++) {
  let isContinuous = false;

  for (let j = 0; j < M; j++) {
    const curDecoration = floor[i][j];

    if (curDecoration === "-" && !isContinuous) {
      answer += 1;
      isContinuous = true;
    } else if (curDecoration === "|") {
      isContinuous = false;
    }
  }
}

for (let i = 0; i < M; i++) {
  let isContinuous = false;

  for (let j = 0; j < N; j++) {
    const curDecoration = floor[j][i];

    if (curDecoration === "|" && !isContinuous) {
      answer += 1;
      isContinuous = true;
    } else if (curDecoration === "-") {
      isContinuous = false;
    }
  }
}

console.log(answer);
