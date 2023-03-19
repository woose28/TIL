const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, ..._positions] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const positions = _positions.map((position) => position.split(" ").map(Number));

positions.sort(([x1, y1], [x2, y2]) => {
  if (x1 > x2) {
    return 1;
  } else if (x1 < x2) {
    return -1;
  } else {
    if (y1 > y2) {
      return 1;
    }

    return -1;
  }
});

console.log(positions.map((position) => position.join(" ")).join("\n"));
