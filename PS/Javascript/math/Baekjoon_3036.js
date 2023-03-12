const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

function getGcd(a, b) {
  if (b === 0) {
    return a;
  }

  return getGcd(b, a % b);
}

const [_N, _rings] = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(_N);
const rings = _rings.split(" ").map(Number);

const firstRing = rings.shift();

const answer = [];

rings.forEach((ring) => {
  const gcd = getGcd(firstRing, ring);

  answer.push(String(firstRing / gcd) + "/" + String(ring / gcd));
});

console.log(answer.join("\n"));
