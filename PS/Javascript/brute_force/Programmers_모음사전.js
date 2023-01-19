function solution(word) {
  var answer = 0;

  const alphabetList = ["A", "E", "I", "O", "U"];

  const firstAlphabet = word[0];
  let isFind = false;

  const calculateWordCount = (a, n, r) => (a * (Math.pow(r, n) - 1)) / (r - 1);

  const findWordOrder = (curWord) => {
    if (curWord.length === 6) {
      return;
    } else if (isFind) {
      return;
    }

    answer += 1;

    if (curWord === word) {
      isFind = true;
      return;
    }

    alphabetList.forEach((alphabet) => {
      findWordOrder(curWord + alphabet);
    });
  };

  alphabetList.some((alphabet) => {
    if (alphabet !== firstAlphabet) {
      answer += calculateWordCount(1, 5, 5);
      return false;
    }

    findWordOrder(alphabet);

    return true;
  });

  return answer;
}
