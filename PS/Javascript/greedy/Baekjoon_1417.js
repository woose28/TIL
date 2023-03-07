const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [N, ...numbers] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let answer = 0;

while (true) {
  const [maxIndex, _] = numbers.reduce(
    (acc, current, index) => {
      const [_, accVote] = acc;

      if (accVote <= current) {
        return [index, current];
      }

      return acc;
    },
    [-1, 0]
  );

  if (maxIndex === 0) {
    break;
  }

  answer += 1;
  numbers[0] += 1;
  numbers[maxIndex] -= 1;
}

console.log(answer);
