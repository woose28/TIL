function solution(n) {
  var answer = 0;
  const DIVIDED_NUM = 1000000007;

  if (n === 1) {
    answer = 1;
  } else if (n === 2) {
    answer = 2;
  } else if (n > 2) {
    const dp = new Array(n).fill(0);

    dp[0] = 1;
    dp[1] = 2;

    for (let i = 2; i < n; i++) {
      dp[i] = (dp[i - 2] + dp[i - 1]) % DIVIDED_NUM;
    }

    answer = dp[n - 1] % DIVIDED_NUM;
  }

  return answer;
}
