const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");
const [strN, strWeightList] = data;

const N = Number(strN);
const weightList = strWeightList.split(" ").map(Number);

function solution(N, weightList) {
  const tempWeightList = [...weightList];
  let answer = 0;

  const recursion = (curLength, curScore) => {
    if (curLength === 2) {
      if (answer < curScore) {
        answer = curScore;
      }
      return;
    }

    for (let i = 1; i < curLength - 1; i++) {
      const [removedMarble] = tempWeightList.splice(i, 1);
      const nextScore = curScore + tempWeightList[i - 1] * tempWeightList[i];

      recursion(curLength - 1, nextScore);

      tempWeightList.splice(i, 0, removedMarble);
    }
  };

  recursion(N, 0);

  console.log(answer);
}

solution(N, weightList);
