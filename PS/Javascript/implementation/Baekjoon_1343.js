const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const board = fs.readFileSync(filePath).toString().trim();

const boardA = board.replace(/XXXX/gi, "AAAA");

const result = boardA.replace(/XX/gi, "BB");

if (result.indexOf("X") === -1) {
  console.log(result);
  return;
}

console.log(-1);
