const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [X, Y, N] = data[0].split(" ").map(Number);

for (let i = 1; i <= N; i++) {
  const isFizz = i % X === 0;
  const isBuzz = i % Y === 0;

  if (isFizz && isBuzz) {
    console.log("FizzBuzz");
    continue;
  } else if (isFizz) {
    console.log("Fizz");
    continue;
  } else if (isBuzz) {
    console.log("Buzz");
    continue;
  }

  console.log(i);
}
