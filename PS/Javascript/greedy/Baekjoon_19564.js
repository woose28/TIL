const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const writing = fs.readFileSync(filePath).toString().trim();

let pressingCount = 1;
let currentIndex = 0;

while (currentIndex < writing.length - 1) {
  const currentString = writing[currentIndex];
  const nextString = writing[currentIndex + 1];

  if (currentString >= nextString) {
    pressingCount += 1;
  }

  currentIndex += 1;
}

console.log(pressingCount);
