function solution(n, m, section) {
  var answer = 0;

  let curMaxPos = 0;

  section.forEach((pos) => {
    if (pos > curMaxPos) {
      answer += 1;
      curMaxPos = pos + m - 1;
    }
  });

  return answer;
}
