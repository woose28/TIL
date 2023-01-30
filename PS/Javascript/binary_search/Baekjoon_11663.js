const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = data[0].split(" ").map(Number);
const spots = data[1].split(" ").map(Number);
const segments = data.slice(2);

spots.sort((a, b) => a - b);

const answer = [];

function findStartIndex(target) {
  let left = 0;
  let right = N - 1;

  while (left <= right) {
    const mid = Number.parseInt((left + right) / 2);

    if (spots[mid] > target) {
      right = mid - 1;
    } else if (spots[mid] === target) {
      return mid;
    } else {
      left = mid + 1;
    }
  }

  return left;
}

function findEndIndex(target, startIndex) {
  let left = startIndex;
  let right = N - 1;

  while (left <= right) {
    const mid = Number.parseInt((left + right) / 2);

    if (spots[mid] > target) {
      right = mid - 1;
    } else if (spots[mid] === target) {
      return mid;
    } else {
      left = mid + 1;
    }
  }

  return right;
}

segments.forEach((segment) => {
  const [start, end] = segment.split(" ").map(Number);

  if (start > spots[N - 1] || end < spots[0]) {
    answer.push(0);
    return;
  }

  const startIndex = findStartIndex(start);
  const endIndex = findEndIndex(end, startIndex);

  answer.push(endIndex - startIndex + 1);
});

console.log(answer.join("\n"));
