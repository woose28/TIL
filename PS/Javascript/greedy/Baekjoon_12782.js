const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const [_T, ...testCases] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const answer = [];

testCases.forEach((testCase) => {
  const [someBinary, otherBinary] = testCase
    .split(" ")
    .map((stringBinary) => stringBinary.split(""));

  let diffCountZero = 0;
  let diffCountOne = 0;

  someBinary.forEach((someNumber, index) => {
    const otherNumber = otherBinary[index];

    if (someNumber === otherNumber) {
      return;
    }

    if (someNumber === "1") {
      diffCountOne += 1;
    } else if (someNumber === "0") {
      diffCountZero += 1;
    }
  });

  const friendshipBit =
    Math.min(diffCountZero, diffCountOne) +
    Math.abs(diffCountZero - diffCountOne);

  answer.push(friendshipBit);
});

console.log(answer.join("\n"));
