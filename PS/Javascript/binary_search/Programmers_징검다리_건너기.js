function solution(stones, k) {
  var answer = 0;

  let left = 1,
    right = 200000000;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let skippedCount = 0;

    for (let stone of stones) {
      if (stone > mid) {
        skippedCount = 0;
        continue;
      }

      skippedCount += 1;

      if (skippedCount === k) {
        break;
      }
    }

    if (skippedCount < k) {
      left = mid + 1;
      answer = left;
      continue;
    }

    right = mid - 1;
  }

  return answer;
}
