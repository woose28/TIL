const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const solution = (input) => {
  let [n, m] = input[0].split(" ").map((char) => Number(char));

  const needMList = [];
  let answer = 0;

  for (let i = 0; i < n; i++) {
    const [p, l] = input[i * 2 + 1].split(" ").map((char) => Number(char));
    const mList = input[i * 2 + 2].split(" ").map((char) => Number(char));

    if (p < l) {
      needMList.push(1);
      continue;
    }

    mList.sort((a, b) => a - b);
    needMList.push(mList[p - l]);
  }

  needMList.sort((a, b) => a - b);

  needMList.forEach((needM) => {
    if (needM <= m) {
      m -= needM;
      answer += 1;
    }
  });

  console.log(answer);
};

solution(input);
