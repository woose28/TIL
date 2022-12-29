function solution(user_id, banned_id) {
  var answer = 0;
  const answerList = [];

  const regExps = banned_id.map(
    (id) => new RegExp("^" + id.replaceAll("*", ".") + "$")
  );
  const bannedCount = banned_id.length;
  const userCount = user_id.length;

  const matches = new Array(bannedCount).fill(0).map(() => new Array());

  regExps.forEach((regExp, index) => {
    user_id.forEach((id, idIndex) => {
      if (regExp.test(id)) {
        matches[index].push(idIndex);
      }
    });
  });

  const used = new Array(userCount).fill(false);

  function recursion(curIdx, selected) {
    if (curIdx === bannedCount) {
      selected.sort((a, b) => a - b);

      const stringCandidate = selected.join("");

      const result = answerList.every(
        (answerCandidate) => stringCandidate !== answerCandidate
      );

      if (result) {
        answerList.push(stringCandidate);
      }

      return;
    }

    const matchIds = matches[curIdx];

    matchIds.forEach((idIndex) => {
      if (!used[idIndex]) {
        used[idIndex] = true;
        selected.push(idIndex);

        recursion(curIdx + 1, [...selected]);

        selected.pop();
        used[idIndex] = false;
      }
    });
  }

  recursion(0, []);

  answer = answerList.length;

  return answer;
}
