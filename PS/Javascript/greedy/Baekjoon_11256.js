const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(data.shift());

const answers = [];

for (let i = 0; i < T; i++) {
  let [J, N] = data.shift().split(" ").map(Number);

  const boxes = [];

  for (let j = 0; j < N; j++) {
    const [R, C] = data.shift().split(" ").map(Number);

    boxes.push(R * C);
  }

  boxes.sort((a, b) => b - a);

  let usingBoxCount = 0;

  boxes.some((box) => {
    usingBoxCount += 1;

    J -= box;

    const isBreak = J <= 0;

    return isBreak;
  });

  answers.push(usingBoxCount);
}

console.log(answers.join("\n"));
