function solution(s) {
  var answer = 0;
  const n = s.length;

  for (let i = 0; i < n; i++) {
    const bracketStack = [];
    let isSuccess = true;

    for (let j = 0; j < n; j++) {
      const curIdx = (i + j) % n;
      const curBracket = s[curIdx];

      if (curBracket === "[" || curBracket === "(" || curBracket === "{") {
        bracketStack.push(curBracket);
        continue;
      }

      if (bracketStack.length === 0) {
        isSuccess = false;
        break;
      }

      const lastOpenBracket = bracketStack.pop();

      if (curBracket === "]") {
        if (lastOpenBracket !== "[") {
          isSuccess = false;
          break;
        }
      } else if (curBracket === ")") {
        if (lastOpenBracket !== "(") {
          isSuccess = false;
          break;
        }
      } else if (curBracket === "}") {
        if (lastOpenBracket !== "{") {
          isSuccess = false;
          break;
        }
      }
    }

    if (isSuccess && bracketStack.length === 0) {
      answer += 1;
    }
  }

  return answer;
}
