const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [N, ...numbers] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

numbers.sort((a, b) => a - b);

const answers = [0, 0, 0, 0];

answers[1] = numbers[Number.parseInt(N / 2)];
answers[3] = numbers[N - 1] - numbers[0];

const numberHash = new Map();

const accumulativeSum = numbers.reduce((acc, currentNumber) => {
  if (numberHash.has(currentNumber)) {
    numberHash.set(currentNumber, numberHash.get(currentNumber) + 1);
  } else {
    numberHash.set(currentNumber, 1);
  }

  return acc + currentNumber;
}, 0);

answers[0] = Math.round(accumulativeSum / N);

const numberHashKeyValue = Array.from(numberHash.entries());
numberHashKeyValue.sort((a, b) => {
  if (a[1] > b[1]) {
    return -1;
  }
  if (a[1] < b[1]) {
    return 1;
  } else {
    if (a[0] > b[0]) {
      return 1;
    } else {
      return -1;
    }
  }
});

if (
  numberHashKeyValue.length > 1 &&
  numberHashKeyValue[0][1] === numberHashKeyValue[1][1]
) {
  answers[2] = numberHashKeyValue[1][0];
} else {
  answers[2] = numberHashKeyValue[0][0];
}

console.log(answers.join("\n"));
