const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [_N, ..._sides] = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(_N);

const d = [
  [1, 0],
  [-1, 0],
  [0, -1],
  [0, 1],
];

const posX = new Set([]);
const posY = new Set([]);

let cx = 0;
let cy = 0;

const sideTypes = [0, 0, 0, 0];

let area = 0;

_sides.forEach((_side) => {
  const [sideType, sideLength] = _side.split(" ").map(Number);
  const [dx, dy] = d[sideType - 1];

  const nx = cx + sideLength * dx;
  const ny = cy + sideLength * dy;

  posX.add(nx);
  posY.add(ny);

  sideTypes[sideType - 1] += 1;

  cx = nx;
  cy = ny;
});

const mapType = sideTypes.reduce((acc, sideType, index) => {
  if (index === 0) {
    return 0;
  }

  return acc + sideType * (index + 1);
}, 0);

const sortedX = Array.from(posX);
const sortedY = Array.from(posY);

sortedX.sort((a, b) => a - b);
sortedY.sort((a, b) => a - b);

const bigRectArea =
  Math.abs(sortedX[2] - sortedX[0]) * Math.abs(sortedY[2] - sortedY[0]);

if (mapType === 12) {
  const smallRectArea =
    Math.abs(sortedX[1] - sortedX[0]) * Math.abs(sortedY[1] - sortedY[0]);

  area = bigRectArea - smallRectArea;
} else if (mapType === 15) {
  const smallRectArea =
    Math.abs(sortedX[2] - sortedX[1]) * Math.abs(sortedY[2] - sortedY[1]);
  area = bigRectArea - smallRectArea;
} else if (mapType === 13) {
  const smallRectArea =
    Math.abs(sortedX[2] - sortedX[1]) * Math.abs(sortedY[1] - sortedY[0]);
  area = bigRectArea - smallRectArea;
} else if (mapType === 14) {
  const smallRectArea =
    Math.abs(sortedX[1] - sortedX[0]) * Math.abs(sortedY[2] - sortedY[1]);
  area = bigRectArea - smallRectArea;
}

console.log(N * area);
