const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [L, R] = fs.readFileSync(filePath).toString().trim().split(" ");

let answer = 0;

if (L.length === R.length) {
  for (let i = 0; i < R.length; i++) {
    if (L[i] !== R[i]) {
      break;
    }

    if (L[i] === "8") {
      answer += 1;
    }
  }
}

console.log(answer);
