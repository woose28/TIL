function getDivisorCount(num) {
  const divisors = [];

  for (let i = 1; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      divisors.push(i);

      if (num / i !== i) {
        divisors.push(num / i);
      }
    }
  }

  return divisors.length;
}

function solution(number, limit, power) {
  var answer = 0;

  const divisorCounts = new Array(number).fill(0).map((_, index) => {
    return getDivisorCount(index + 1);
  });

  answer = divisorCounts.reduce((acc, divisorCount) => {
    const steelWeight = divisorCount > limit ? power : divisorCount;

    return acc + steelWeight;
  }, 0);

  return answer;
}
