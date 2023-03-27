const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [P, N] = data.shift().split(" ").map(Number);
const accessoriesP = data[0].split(" ").map(Number);

accessoriesP.sort((a, b) => a - b);

let answer = 0;
const limitP = 200;
let accumulativeP = P;

accessoriesP.some((accessoryP) => {
  if (accumulativeP >= limitP) {
    return true;
  }

  answer += 1;
  accumulativeP += accessoryP;
  return false;
});

console.log(answer);
