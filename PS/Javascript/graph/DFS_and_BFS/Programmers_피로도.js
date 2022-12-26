function solution(k, dungeons) {
  var answer = -1;
  const countDungeon = dungeons.length;

  const visited = new Array(countDungeon).fill(false);

  function recursion(curK, visitedCount) {
    answer = Math.max(answer, visitedCount);

    for (let i = 0; i < countDungeon; i++) {
      const [reqK, conK] = dungeons[i];

      if (curK >= reqK && !visited[i]) {
        visited[i] = true;
        recursion(curK - conK, visitedCount + 1);
        visited[i] = false;
      }
    }
  }

  for (let i = 0; i < countDungeon; i++) {
    const [reqK, conK] = dungeons[i];

    if (k >= reqK && !visited[i]) {
      visited[i] = true;
      recursion(k - conK, 1);
      visited[i] = false;
    }
  }

  return answer;
}
