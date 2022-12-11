function solution(survey, choices) {
  var answer = "";

  const result = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  };

  choices.forEach((choice, index) => {
    const [n, y] = survey[index].split("");

    if (choice <= 3) {
      result[n] += 4 - choice;
      return;
    }

    result[y] += choice - 4;
  });

  answer += result["R"] >= result["T"] ? "R" : "T";
  answer += result["C"] >= result["F"] ? "C" : "F";
  answer += result["J"] >= result["M"] ? "J" : "M";
  answer += result["A"] >= result["N"] ? "A" : "N";

  return answer;
}
