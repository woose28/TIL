const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim();

const answer = data
  .split("")
  .sort((a, b) => b - a)
  .join("");

console.log(answer);
