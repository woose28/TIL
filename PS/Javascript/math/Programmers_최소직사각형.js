function solution(sizes) {
  var answer = 0;

  let maxLongerLength = 0;
  let maxShorterLength = 0;

  sizes.forEach((size) => {
    const [shorter, longer] = size.sort((a, b) => a - b);

    if (longer > maxLongerLength) {
      maxLongerLength = longer;
    }

    if (shorter > maxShorterLength) {
      maxShorterLength = shorter;
    }
  });

  answer = maxLongerLength * maxShorterLength;

  return answer;
}
