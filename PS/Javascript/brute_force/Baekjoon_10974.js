const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim();

function solution(data) {
  const N = Number(data);
  const isSelectedList = new Array(N).fill(false);
  const resultList = [];
  const answerList = [];

  const recursion = (selectedCount) => {
    if (selectedCount === N) {
      answerList.push(resultList.join(" "));
      return;
    }

    isSelectedList.forEach((isSelected, index) => {
      if (!isSelected) {
        isSelectedList[index] = true;
        resultList.push(index + 1);

        recursion(selectedCount + 1);

        resultList.pop();
        isSelectedList[index] = false;
      }
    });
  };

  recursion(0, "");

  console.log(answerList.join("\n"));
}

solution(data);
