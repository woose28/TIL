const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(data.shift());

const fans = data.map((fan) => fan.split(" ").map(Number));

const [maxStartTime, minEndTime] = fans.reduce(
  (acc, [currentStartTime, currentEndTime]) => {
    const [maxStartTime, minEndTime] = acc;

    if (maxStartTime < currentStartTime) {
      acc[0] = currentStartTime;
    }

    if (minEndTime > currentEndTime) {
      acc[1] = currentEndTime;
    }

    return acc;
  },
  [0, Infinity]
);

const answer = Math.max(0, maxStartTime - minEndTime);

console.log(answer);
