const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

let [N, K, L] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let round = 1;

while (true) {
  const nextK = (K % 2) + Number.parseInt(K / 2);
  const nextL = (L % 2) + Number.parseInt(L / 2);

  if (nextK === nextL) {
    break;
  }

  round += 1;
  K = nextK;
  L = nextL;
}

console.log(round);
