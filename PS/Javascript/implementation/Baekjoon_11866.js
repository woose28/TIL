const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const [N, K] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const answer = [];

const people = new Array(N).fill(0).map((_, index) => index + 1);
let currentIndex = -1;

for (let i = 0; i < N; i++) {
  const removedIndex = (currentIndex + K) % people.length;

  const [removedPerson] = people.splice(removedIndex, 1);

  answer.push(removedPerson);

  currentIndex = (removedIndex - 1) % people.length;
}

console.log(`<${answer.join(", ")}>`);
