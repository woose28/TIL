function solution(dots) {
  var answer = 0;

  for (let i = 0; i < 3; i++) {
    for (let j = i + 1; j <= 3; j++) {
      const dot1 = dots[i];
      const dot2 = dots[j];

      const [dot3, dot4] = dots.filter(
        (_, index) => index !== i && index !== j
      );

      const inclination1 = (dot1[1] - dot2[1]) / (dot1[0] - dot2[0]);
      const inclination2 = (dot3[1] - dot4[1]) / (dot3[0] - dot4[0]);

      if (inclination1 === inclination2) {
        answer = 1;
        break;
      }
    }

    if (answer === 1) {
      break;
    }
  }

  return answer;
}
