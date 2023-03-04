const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M, K] = data[0].split(" ").map(Number);

const arr = new Array(N).fill(0).map((_, index) => BigInt(data[index + 1]));

const tree = new Array(N * 4);

function init(node, start, end) {
  if (start === end) {
    tree[node] = arr[start];
    return;
  }

  const mid = Number.parseInt((start + end) / 2);

  init(node * 2, start, mid);
  init(node * 2 + 1, mid + 1, end);
  tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

function query(node, start, end, left, right) {
  if (left > end || right < start) {
    return BigInt(0);
  } else if (left <= start && end <= right) {
    return tree[node];
  }

  const mid = Number.parseInt((start + end) / 2);

  const leftSum = query(node * 2, start, mid, left, right);
  const rightSum = query(node * 2 + 1, mid + 1, end, left, right);

  return leftSum + rightSum;
}

function update(index, val) {
  const diff = BigInt(val) - arr[index];
  arr[index] = BigInt(val);

  updateTree(1, 0, N - 1, index, diff);
}

function updateTree(node, start, end, index, diff) {
  if (index < start || index > end) {
    return;
  }

  tree[node] += diff;

  if (start !== end) {
    const mid = Number.parseInt((start + end) / 2);

    updateTree(node * 2, start, mid, index, diff);
    updateTree(node * 2 + 1, mid + 1, end, index, diff);
  }
}

const answer = [];

init(1, 0, N - 1);

for (let i = N + 1; i < N + M + K + 1; i++) {
  const [a, b, c] = data[i].split(" ").map(Number);

  if (a === 1) {
    update(b - 1, c);
    continue;
  }

  const sumResult = query(1, 0, N - 1, b - 1, c - 1);

  answer.push(sumResult);
}

console.log(answer.join("\n"));
