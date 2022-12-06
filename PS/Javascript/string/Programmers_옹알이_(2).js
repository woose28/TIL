function isPronounce(testCase) {
  let curIdx = 0;
  let recentKind = 0;

  while (curIdx < testCase.length) {
    if (testCase[curIdx] === "a") {
      if (recentKind === "a" || testCase.slice(curIdx, curIdx + 3) !== "aya") {
        return false;
      }

      recentKind = "a";
      curIdx += 3;
    } else if (testCase[curIdx] === "y") {
      if (recentKind === "y" || testCase.slice(curIdx, curIdx + 2) !== "ye") {
        return false;
      }

      recentKind = "y";
      curIdx += 2;
    } else if (testCase[curIdx] === "w") {
      if (recentKind === "w" || testCase.slice(curIdx, curIdx + 3) !== "woo") {
        return false;
      }

      recentKind = "w";
      curIdx += 3;
    } else if (testCase[curIdx] === "m") {
      if (recentKind === "m" || testCase.slice(curIdx, curIdx + 2) !== "ma") {
        return false;
      }

      recentKind = "m";
      curIdx += 2;
    } else {
      return false;
    }
  }

  return true;
}

function solution(babbling) {
  var answer = 0;

  for (const testCase of babbling) {
    if (isPronounce(testCase)) {
      console.log(testCase);
      answer += 1;
    }
  }

  return answer;
}
