const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const lights = fs.readFileSync(filePath).toString().trim().split("");

const lightCount = lights.length;

let answer = 0;

for (let i = 1; i <= lightCount; i++) {
  const light = lights[i - 1];

  if (light === "Y") {
    answer += 1;

    for (let j = 1; j <= lightCount; j++) {
      if (j * i > lightCount) {
        break;
      }

      lights[i * j - 1] = lights[i * j - 1] === "Y" ? "N" : "Y";
    }
  }
}

console.log(answer);
