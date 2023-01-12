function solution(s) {
  var answer = true;

  const bracketStack = [];

  for (let i = 0; i < s.length; i++) {
    const curBracket = s[i];

    if (curBracket === "(") {
      bracketStack.push("(");
    } else if (curBracket === ")") {
      const poppedBracket = bracketStack.pop();

      if (poppedBracket !== "(") {
        answer = false;
        break;
      }
    }
  }

  if (bracketStack.length !== 0) {
    answer = false;
  }

  return answer;
}
