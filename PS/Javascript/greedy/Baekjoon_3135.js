const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_AB, _N, ..._favorites] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [A, B] = _AB.split(" ").map(Number);
const favorites = _favorites.map(Number);

let answer = 0;

let nearestFrequency = A;

favorites.forEach((favorite) => {
  if (Math.abs(B - nearestFrequency) > Math.abs(B - favorite)) {
    nearestFrequency = favorite;
  }
});

if (A !== nearestFrequency) {
  answer += 1;
}

answer += Math.abs(B - nearestFrequency);

console.log(answer);
