function solution(alp, cop, problems) {
  var answer = 0;

  let maxAlp = alp;
  let maxCop = cop;

  problems.forEach((problem) => {
    const [alp_req, cop_req] = problem;

    maxAlp = Math.max(maxAlp, alp_req);
    maxCop = Math.max(maxCop, cop_req);
  });

  const dp = new Array(maxAlp - alp + 1)
    .fill(0)
    .map(() => new Array(maxCop - cop + 1).fill(Infinity));

  dp[0][0] = 0;

  dp.forEach((row, ri) => {
    row.forEach((e, ci) => {
      problems.forEach((problem) => {
        const [alp_req, cop_req, alp_rwd, cop_rwd, cost] = problem;

        if (ri + alp >= alp_req && ci + cop >= cop_req) {
          const nr = Math.min(ri + alp_rwd, dp.length - 1);
          const nc = Math.min(ci + cop_rwd, row.length - 1);

          dp[nr][nc] = Math.min(dp[nr][nc], dp[ri][ci] + cost);
        }
      });

      if (ri < dp.length - 1) {
        dp[ri + 1][ci] = Math.min(dp[ri + 1][ci], dp[ri][ci] + 1);
      }

      if (ci < row.length - 1) {
        dp[ri][ci + 1] = Math.min(dp[ri][ci + 1], dp[ri][ci] + 1);
      }
    });
  });

  answer = dp[dp.length - 1][dp[0].length - 1];

  return answer;
}
