const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const inputtedString = fs.readFileSync(filePath).toString().trim();

function isPalindrome(text) {
  if (text.length === 1) {
    return true;
  }

  const centeredIndex = Number.parseInt(text.length / 2);

  const halfFrontText = text.slice(0, centeredIndex);
  const halfBackText =
    text.length % 2 === 0
      ? text.slice(centeredIndex)
      : text.slice(centeredIndex + 1);

  const reversedHalfBackText = halfBackText.split("").reverse().join("");

  if (halfFrontText !== reversedHalfBackText) {
    return false;
  }

  return true;
}

let answer = inputtedString.length;

for (let i = 0; i < inputtedString.length; i++) {
  const appendedString = inputtedString
    .slice(0, i)
    .split("")
    .reverse()
    .join("");

  const newString = inputtedString + appendedString;

  if (isPalindrome(newString)) {
    answer = newString.length;
    break;
  }
}

console.log(answer);
