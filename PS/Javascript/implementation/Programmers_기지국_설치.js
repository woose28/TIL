function solution(n, stations, w) {
  var answer = 0;

  const coverCount = w * 2 + 1;
  let prevEnd = 0;

  stations.forEach((station) => {
    const uncoveredCount = station - w - prevEnd - 1;

    if (uncoveredCount > 0) {
      answer += Math.ceil(uncoveredCount / coverCount);
    }

    prevEnd = station + w;
  });

  if (prevEnd < n) {
    const uncoveredCount = n - prevEnd;
    answer += Math.ceil(uncoveredCount / coverCount);
  }

  return answer;
}
