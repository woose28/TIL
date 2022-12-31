const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";
const data = fs.readFileSync(filePath).toString().trim();

const answer = [];
const [N, M] = data.split(" ").map(Number);

function combination(lastIndex, selected) {
  if (selected.length === M) {
    answer.push(selected.join(" "));
    return;
  }

  for (let i = lastIndex + 1; i <= N; i++) {
    selected.push(i);

    combination(i, selected);

    selected.pop();
  }
}

combination(0, []);

console.log(answer.join("\n"));
