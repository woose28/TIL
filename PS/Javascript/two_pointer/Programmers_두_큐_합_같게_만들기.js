function solution(queue1, queue2) {
  var answer = -1;

  const copiedQ1 = queue1.slice();
  const copiedQ2 = queue2.slice();

  let sumQ1 = copiedQ1.reduce((acc, element) => acc + element);
  let sumQ2 = copiedQ2.reduce((acc, element) => acc + element);

  if ((sumQ1 + sumQ2) % 2 !== 0) {
    return answer;
  }

  const totalQueue = [...copiedQ1, ...copiedQ2];
  let rp = 0;
  let lp = copiedQ1.length;

  const maxCnt = copiedQ1.length * 2 + 2;
  let curCnt = 0;

  while (curCnt <= maxCnt) {
    if (sumQ1 === sumQ2) {
      answer = curCnt;
      break;
    } else if (sumQ1 > sumQ2) {
      sumQ1 -= totalQueue[rp];
      sumQ2 += totalQueue[rp];
      rp = (rp + 1) % totalQueue.length;
    } else {
      sumQ2 -= totalQueue[lp];
      sumQ1 += totalQueue[lp];
      lp = (lp + 1) % totalQueue.length;
    }
    curCnt += 1;
  }

  return answer;
}
