function solution(n) {
  var answer = 0;

  const nBinary = n.toString(2);

  function findOneCount(binary) {
    return binary
      .split("")
      .reduce((acc, bit) => (bit === "1" ? acc + 1 : acc), 0);
  }

  const oneCount = findOneCount(nBinary);

  for (let i = n + 1; i <= 1000000; i++) {
    const newBinary = i.toString(2);

    if (oneCount === findOneCount(newBinary)) {
      answer = i;
      break;
    }
  }

  return answer;
}
