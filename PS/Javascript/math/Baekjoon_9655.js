const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

if (data % 2 === 0) {
  console.log("CY");
} else {
  console.log("SK");
}
