function solution(lines) {
  var answer = 0;

  function calculateOverlappedLength(startPots, endPots) {
    const maxStartPot = Math.max(...startPots);

    const minEndPot = Math.min(...endPots);

    if (maxStartPot < minEndPot) {
      return Math.abs(minEndPot - maxStartPot);
    }

    return 0;
  }

  for (let i = 0; i < 3; i++) {
    const otherLineIndex = (i + 1) % 3;

    const result = calculateOverlappedLength(
      [lines[i][0], lines[otherLineIndex][0]],
      [lines[i][1], lines[otherLineIndex][1]]
    );

    console.log("", result);
    answer += result;
  }

  answer -=
    calculateOverlappedLength(
      lines.map(([start, end]) => start),
      lines.map(([start, end]) => end)
    ) * 2;

  return answer;
}
