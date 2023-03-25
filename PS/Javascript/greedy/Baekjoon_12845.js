const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());
const cards = data[0].split(" ").map(Number);

cards.sort((a, b) => b - a);

const maxCard = cards.shift();
const answer = cards.reduce(
  (acc, currentCard) => acc + currentCard + maxCard,
  0
);

console.log(answer);
