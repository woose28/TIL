const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [NM, ...strings] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = NM.split(" ").map(Number);

const stringSet = new Set(strings.slice(0, N));
const checkStringList = strings.slice(N);

let answer = 0;

checkStringList.forEach((string) => {
  if (stringSet.has(string)) {
    answer += 1;
  }
});

console.log(answer);
