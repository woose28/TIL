function solution(n, s) {
  var answer = [];

  if (n > s) {
    return [-1];
  }

  let cn = n;
  let cs = s;

  while (cn > 0) {
    const ne = Math.floor(cs / cn);

    answer.push(ne);

    cn = cn - 1;
    cs = cs - ne;
  }

  answer.sort((a, b) => a - b);

  return answer;
}
