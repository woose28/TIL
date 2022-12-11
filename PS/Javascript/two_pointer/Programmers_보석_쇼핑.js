function solution(gems) {
  var answer = [1, gems.length];

  const gemKind = new Set(gems);
  const gemKindCount = gemKind.size;

  const gemCount = new Map();

  let start = 0,
    end = 0;

  gemCount.set(gems[0], 1);

  while (end < gems.length) {
    if (gemCount.size !== gemKindCount) {
      end += 1;

      const curGem = gems[end];
      gemCount.set(curGem, gemCount.has(curGem) ? gemCount.get(curGem) + 1 : 1);
      continue;
    }

    if (answer[1] - answer[0] > end - start) {
      answer = [start + 1, end + 1];
    }

    const removedGem = gems[start];

    gemCount.set(removedGem, gemCount.get(removedGem) - 1);

    if (gemCount.get(removedGem) === 0) {
      gemCount.delete(removedGem);
    }

    start += 1;
  }

  return answer;
}
