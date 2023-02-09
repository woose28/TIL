const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const N = Number(fs.readFileSync(filePath).toString().trim());

const cards = new Array(N).fill(0).map((_, index) => index + 1);

const answers = [];

while (cards.length > 1) {
  const removedCard = cards.shift();
  const toBottomCard = cards.shift();

  answers.push(removedCard);
  cards.push(toBottomCard);
}

if (N === 1) {
  console.log(1);
} else {
  console.log(`${answers.join(" ")} ${cards[0]}`);
}
