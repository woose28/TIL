const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());

const queries = data.map((query) => {
  const [_queryNumbers, strikeCount, ballCount] = query.split(" ");

  const queryNumbers = _queryNumbers.split("").map(Number);

  return [queryNumbers, Number(strikeCount), Number(ballCount)];
});

let answer = 0;

for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    if (i === j) {
      continue;
    }

    for (let k = 1; k <= 9; k++) {
      if (i === k || j === k) {
        continue;
      }

      const currentNumbers = [i, j, k];

      const isAllPass = queries.every(
        ([queryNumbers, strikeCount, ballCount]) => {
          const [currentStrikeCount, currentBallCount] = queryNumbers.reduce(
            (acc, queryNumber, index) => {
              const currentNumber = currentNumbers[index];

              if (queryNumber === currentNumber) {
                acc[0] += 1;
              } else if (currentNumbers.includes(queryNumber)) {
                acc[1] += 1;
              }

              return acc;
            },
            [0, 0]
          );

          if (
            strikeCount !== currentStrikeCount ||
            ballCount !== currentBallCount
          ) {
            return false;
          }

          return true;
        }
      );

      if (isAllPass) {
        answer += 1;
      }
    }
  }
}

console.log(answer);
