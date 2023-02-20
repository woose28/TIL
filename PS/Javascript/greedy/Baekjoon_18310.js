const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, _houses] = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(_N);
const houses = _houses.split(" ").map(Number);

houses.sort((a, b) => a - b);

let answer = 0;

let previousHousePos = houses[0];

let previousTotalDistance = houses.reduce(
  (acc, house) => acc + (house - previousHousePos),
  0
);

answer = previousHousePos;

houses.forEach((house, index) => {
  const distance = house - previousHousePos;

  const currentTotalDistance =
    previousTotalDistance + (index - 0) * distance - (N - index) * distance;

  if (previousTotalDistance > currentTotalDistance) {
    answer = house;
  }

  previousHousePos = house;
});

console.log(answer);
