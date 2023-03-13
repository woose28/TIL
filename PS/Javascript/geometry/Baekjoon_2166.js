const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, ..._positions] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = Number(_N);
const positions = _positions.map((_position) =>
  _position.split(" ").map(Number)
);

const [accFront, accBack] = positions.reduce(
  ([accFront, accBack], [cx, cy], index) => {
    const [nx, ny] = positions[(index + 1) % N];

    return [accFront + cx * ny, accBack + cy * nx];
  },
  [0, 0]
);

const answer = (
  Math.round((Math.abs(accFront - accBack) / 2) * 10) / 10
).toFixed(1);

console.log(answer);
