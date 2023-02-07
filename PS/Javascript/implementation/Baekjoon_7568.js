const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, ..._people] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = Number(_N);
const people = _people.map((person) => person.split(" ").map(Number));

const answer = [];

people.forEach((me, myIndex) => {
  let rank = 1;

  people.forEach((other, othersIndex) => {
    if (myIndex === othersIndex) {
      return;
    }

    if (me[0] < other[0] && me[1] < other[1]) {
      rank += 1;
    }
  });

  answer.push(rank);
});

console.log(answer.join(" "));
