function solution(n, info) {
  var answer = [-1];
  let maxDiff = 0;

  function compareScore(lionInfo) {
    const scoreDiff = lionInfo.reduce((acc, lionShot, index) => {
      const apeachShot = info[index];

      if (lionShot === 0 && apeachShot === 0) {
        return acc;
      } else if (lionShot > apeachShot) {
        return acc + (10 - index);
      }

      return acc - (10 - index);
    }, 0);

    const isLionWin = scoreDiff > 0;

    return [isLionWin, scoreDiff];
  }

  function recursion(remain, index, lionInfo) {
    if (index < -1) {
      return;
    }

    if (remain === 0) {
      const [isLionWin, scoreDiff] = compareScore(lionInfo);

      if (!isLionWin) {
        return;
      }

      if (maxDiff < scoreDiff) {
        answer = [...lionInfo];
        maxDiff = scoreDiff;
      } else if (maxDiff === scoreDiff) {
        let haveToChange = false;

        for (let i = 10; i >= 0; i--) {
          if (answer[i] < lionInfo[i]) {
            haveToChange = true;
            break;
          } else if (answer[i] > lionInfo[i]) {
            break;
          }
        }

        if (haveToChange) {
          answer = [...lionInfo];
        }
      }

      return;
    }

    for (let i = 0; i <= remain; i++) {
      const newLionInfo = [...lionInfo];

      newLionInfo[index] += i;

      recursion(remain - i, index - 1, newLionInfo);
    }
  }

  recursion(n, 10, new Array(11).fill(0));

  return answer;
}
