function solution(N, number) {
  const minNumCountMap = new Map();
  const nCountNums = new Array(8).fill(0).reduce((acc, _, index) => {
    acc.set(index + 1, []);

    return acc;
  }, new Map());

  if (N === number) {
    return 1;
  }

  let answer = 9;

  nCountNums.get(1).push(N);
  minNumCountMap.set(N, 1);

  for (let i = 2; i < 9; i++) {
    const iCountNums = nCountNums.get(i);
    const nSequenceNum = Number(String(N).repeat(i));

    if (!minNumCountMap.get(nSequenceNum)) {
      minNumCountMap.set(nSequenceNum, i);
      iCountNums.push(nSequenceNum);
    }

    for (let j = 1; j < i; ++j) {
      for (const num1 of nCountNums.get(j)) {
        for (const num2 of nCountNums.get(i - j)) {
          const plusResult = num1 + num2;
          const minusResult = num1 - num2;
          const multiplyResult = num1 * num2;
          const divideResult = Number.parseInt(num1 / num2);

          if (!minNumCountMap.get(plusResult)) {
            minNumCountMap.set(plusResult, i);
            iCountNums.push(plusResult);
          }

          if (!minNumCountMap.get(minusResult)) {
            minNumCountMap.set(minusResult, i);
            iCountNums.push(minusResult);
          }

          if (!minNumCountMap.get(multiplyResult)) {
            minNumCountMap.set(multiplyResult, i);
            iCountNums.push(multiplyResult);
          }

          if (
            !minNumCountMap.get(divideResult) &&
            !Number.isNaN(divideResult)
          ) {
            minNumCountMap.set(divideResult, i);
            iCountNums.push(divideResult);
          }
        }
      }
    }

    if (iCountNums.find((iCountNum) => iCountNum === number)) {
      answer = i;
      break;
    }
  }

  return answer === 9 ? -1 : answer;
}
