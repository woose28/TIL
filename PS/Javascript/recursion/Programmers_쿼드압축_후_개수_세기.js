function solution(arr) {
  var answer = [0, 0];

  const n = arr.length;

  function recursion(sr, sc, er, ec, cn) {
    const firstNum = arr[sr][sc];
    let isAllSame = true;

    for (let i = sr; i <= er; i++) {
      for (let j = sc; j <= ec; j++) {
        if (arr[i][j] !== firstNum) {
          isAllSame = false;
          break;
        }
      }

      if (!isAllSame) {
        break;
      }
    }

    if (isAllSame) {
      answer[firstNum] += 1;
      return;
    }

    const nn = cn / 2;
    const br = sr + nn - 1;
    const bc = sc + nn - 1;

    recursion(sr, sc, br, bc, nn);
    recursion(sr, bc + 1, br, ec, nn);
    recursion(br + 1, sc, er, bc, nn);
    recursion(br + 1, bc + 1, er, ec, nn);
  }

  recursion(0, 0, n - 1, n - 1, n);

  return answer;
}
