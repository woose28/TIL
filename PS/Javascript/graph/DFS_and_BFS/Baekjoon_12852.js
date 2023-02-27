// 시간 초과 날 거 같음..
const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const N = Number(fs.readFileSync(filePath).toString().trim());

const isVisited = new Array(N + 1).fill(false);

queue = [[N, 0, [N]]];

minCount = 0;
numberList = [];

while (queue.length > 0) {
  const [cn, cc, cl] = queue.shift();

  if (cn === 1) {
    minCount = cc;
    numberList = cl;
    break;
  } else if (cn <= 0) {
    continue;
  }

  if (cn % 3 == 0 && !isVisited[cn % 3]) {
    isVisited[cn / 3] = true;
    queue.push([cn / 3, cc + 1, [...cl, cn / 3]]);
  }

  if (cn % 2 == 0 && !isVisited[cn % 2]) {
    isVisited[cn / 2] = true;
    queue.push([cn / 2, cc + 1, [...cl, cn / 2]]);
  }

  if (!isVisited[cn - 1]) {
    isVisited[cn - 1] = true;
    queue.push([cn - 1, cc + 1, [...cl, cn - 1]]);
  }
}

console.log(minCount);
console.log(numberList.join(" "));
