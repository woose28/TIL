const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, _sequence] = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(_N);
const sequence = _sequence.split(" ").map(Number);

let swapPos = -1;

for (let i = N - 1; i > 0; i--) {
  const curNum = sequence[i];
  const prevNum = sequence[i - 1];

  if (curNum < prevNum) {
    swapPos = i - 1;
    break;
  }
}

if (swapPos === -1) {
  console.log(-1);
  return;
}

for (let i = N - 1; i >= swapPos - 1; i--) {
  if (sequence[swapPos] > sequence[i]) {
    let temp = sequence[swapPos];

    sequence[swapPos] = sequence[i];
    sequence[i] = temp;
    break;
  }
}

const prevSequenceFrontPart = sequence.slice(0, swapPos + 1);
const prevSequenceBackPart = sequence.slice(swapPos + 1);
prevSequenceBackPart.sort((a, b) => b - a);

const prevSequence = prevSequenceFrontPart.concat(prevSequenceBackPart);

console.log(prevSequence.join(" "));
