const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [Tstring, ...testCase] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const TNumber = Number(Tstring);

for (let i = 0; i < TNumber; i++) {
  const N = Number(testCase[2 * i]);
  const numberArr = testCase[2 * i + 1].split(" ").map(Number);

  const accumulatedArr = new Array(N + 1).fill(0);

  numberArr.forEach((element, index) => {
    const prevAccumulatedSum = accumulatedArr[index];

    if (prevAccumulatedSum < 0) {
      accumulatedArr[index + 1] = element;
      return;
    } else if (prevAccumulatedSum + element < 0) {
      accumulatedArr[index + 1] = element;
      return;
    }

    accumulatedArr[index + 1] = prevAccumulatedSum + element;
  });

  console.log(Math.max(...accumulatedArr.slice(1)));
}
