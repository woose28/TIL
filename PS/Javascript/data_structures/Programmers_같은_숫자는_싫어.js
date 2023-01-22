function solution(arr) {
  var answer = [arr[0]];

  arr.forEach((element) => {
    if (element !== answer[answer.length - 1]) {
      answer.push(element);
    }
  });

  return answer;
}
