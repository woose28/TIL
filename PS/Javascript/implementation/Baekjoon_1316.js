const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, ...words] = data;

let answer = 0;

words.forEach((word) => {
  const characterSet = new Set();

  let prevCharacter = null;

  for (let character of word) {
    if (prevCharacter === character) {
      continue;
    }

    if (characterSet.has(character)) {
      return;
    }

    characterSet.add(character);
    prevCharacter = character;
  }

  answer += 1;
});

console.log(answer);
