const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_T] = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(_T);

for (let i = 0; i < T; i++) {
  console.log("yes");
}
