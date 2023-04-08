const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const [_sk, _ss, _N] = data.shift().split(" ");

const columToNumber = {
  A: 1,
  B: 2,
  C: 3,
  D: 4,
  E: 5,
  F: 6,
  G: 7,
  H: 8,
};

const numberToColum = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
};

const directionToNumber = {
  B: [-1, 0],
  LB: [-1, -1],
  L: [0, -1],
  LT: [1, -1],
  T: [1, 0],
  RT: [1, 1],
  R: [0, 1],
  RB: [-1, 1],
};

let sk = [columToNumber[_sk[0]] - 1, Number(_sk[1]) - 1];
let ss = [columToNumber[_ss[0]] - 1, Number(_ss[1]) - 1];

data.forEach((direction) => {
  const [dy, dx] = directionToNumber[direction];
  const [cc, cr] = sk;
  const [sc, sr] = ss;

  const nr = cr + dy;
  const nc = cc + dx;

  if (0 <= nr && nr < 8 && 0 <= nc && nc < 8) {
    if (nr === sr && nc === sc) {
      const snr = sr + dy;
      const snc = sc + dx;

      if (0 <= snr && snr < 8 && 0 <= snc && snc < 8) {
        sk = [nc, nr];
        ss = [snc, snr];
      }

      return;
    }

    sk = [nc, nr];
  }
});

console.log(String(numberToColum[sk[0] + 1]) + String(sk[1] + 1));
console.log(String(numberToColum[ss[0] + 1]) + String(ss[1] + 1));
