const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const bracketList = fs.readFileSync(filePath).toString().trim().split("");

let answer = 0;
const bracketStack = [];

bracketList.forEach((bracket, index) => {
  if (bracket === "(") {
    bracketStack.push(bracket);
    return;
  }

  if (bracketList[index - 1] === "(") {
    bracketStack.pop();
    answer += bracketStack.length;
    return;
  }

  bracketStack.pop();
  answer += 1;
});

console.log(answer);
