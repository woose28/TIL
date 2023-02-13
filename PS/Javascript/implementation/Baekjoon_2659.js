const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const numbers = fs.readFileSync(filePath).toString().trim().split(" ");

const MIN_CLOCK_NUMBER = 1111;
const MAX_CLOCK_NUMBER = 9999;

const COUNT_NUMBER = MAX_CLOCK_NUMBER - MIN_CLOCK_NUMBER + 1;
const isClockNumber = new Array(COUNT_NUMBER).fill(true);

const getClockNumber = (numbers) => {
  let clockNumber = numbers.join("");

  for (let i = 0; i <= 3; i++) {
    const shiftedNumber = numbers.shift();
    numbers.push(shiftedNumber);

    const newClockNumber = numbers.join("");

    if (clockNumber > newClockNumber) {
      isClockNumber[Number(clockNumber) - MIN_CLOCK_NUMBER] = false;
      clockNumber = newClockNumber;
    } else if (clockNumber < newClockNumber) {
      isClockNumber[Number(newClockNumber) - MIN_CLOCK_NUMBER] = false;
    }
  }

  return Number(clockNumber);
};

let answer = 0;

const targetClockNumber = getClockNumber(numbers);

for (let i = MIN_CLOCK_NUMBER; i <= targetClockNumber; i++) {
  const currentNumberString = String(i);

  if (currentNumberString.includes("0")) {
    continue;
  }

  if (!isClockNumber[i - MIN_CLOCK_NUMBER]) {
    continue;
  }

  const currentClockNumber = getClockNumber(currentNumberString.split(""));

  if (i === currentClockNumber) {
    answer += 1;
  }
}

console.log(answer);
