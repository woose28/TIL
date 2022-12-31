const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const data = fs.readFileSync(filePath).toString().trim();

const answer = [];
const [N, M] = data.split(" ").map(Number);

const isSelected = new Array(N + 1).fill(false);

function permutation(selected) {
  if (selected.length === M) {
    answer.push(selected.join(" "));
  }

  for (let i = 1; i <= N; i++) {
    if (!isSelected[i]) {
      isSelected[i] = true;
      selected.push(i);
      permutation(selected);
      selected.pop();
      isSelected[i] = false;
    }
  }
}

permutation([]);

console.log(answer.join("\n"));
