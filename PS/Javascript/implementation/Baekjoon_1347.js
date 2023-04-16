const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());

const records = data.shift().split("");

let mat = [["."]];

let direction = 0;

const moving = {
  0: [1, 0],
  1: [0, -1],
  2: [-1, 0],
  3: [0, 1],
};

let pos = [0, 0];

records.forEach((record) => {
  if (record === "L") {
    if (direction - 1 < 0) {
      direction = 3;
      return;
    }

    direction = (direction - 1) % 4;
    return;
  } else if (record === "R") {
    direction = (direction + 1) % 4;
    return;
  }

  const [cr, cc] = pos;
  const [dy, dx] = moving[direction];

  let nr = cr + dy;
  let nc = cc + dx;

  if (direction === 0 && nr >= mat.length) {
    mat.push("#".repeat(mat[0].length).split(""));
  } else if (direction === 1 && nc < 0) {
    mat = mat.map((row) => ["#"].concat(row));
    nc = 0;
  } else if (direction === 2 && nr < 0) {
    mat = ["#".repeat(mat[0].length).split("")].concat(mat);
    nr = 0;
  } else if (direction === 3 && nc >= mat[0].length) {
    mat = mat.map((row) => row.concat("#"));
  }

  mat[nr][nc] = ".";
  pos = [nr, nc];
});

const answer = mat.map((row) => row.join("")).join("\n");

console.log(answer);
