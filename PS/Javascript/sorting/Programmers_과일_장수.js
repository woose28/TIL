function solution(k, m, score) {
  var answer = 0;

  score.sort((a, b) => {
    if (a > b) {
      return -1;
    } else if (a === b) {
      return 0;
    }

    return 1;
  });

  for (let i = 0; i <= score.length - m; i = i + m) {
    answer += score[i + m - 1] * m;
  }

  return answer;
}
