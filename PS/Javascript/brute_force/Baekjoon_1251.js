const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const word = fs.readFileSync(filePath).toString().trim();

let answer = word.slice(0, 2) + word.slice(2).split("").reverse().join("");

for (let i = 0; i < word.length - 2; i++) {
  for (let j = i + 1; j < word.length - 1; j++) {
    const firstSplitWord = word.slice(0, i + 1);
    const secondSplitWord = word.slice(i + 1, j + 1);
    const thirdSplitWord = word.slice(j + 1);

    const newWord =
      firstSplitWord.split("").reverse().join("") +
      secondSplitWord.split("").reverse().join("") +
      thirdSplitWord.split("").reverse().join("");

    if (newWord < answer) {
      answer = newWord;
    }
  }
}

console.log(answer);
