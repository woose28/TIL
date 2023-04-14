function solution(dirs) {
  var answer = 0;

  const visitedMap = new Map();
  const directionMap = {
    U: [1, 0],
    D: [-1, 0],
    R: [0, 1],
    L: [0, -1],
  };

  const pos = [0, 0];

  dirs.split("").forEach((dir) => {
    const [dy, dx] = directionMap[dir];

    const [cr, cc] = pos;

    const nr = cr + dy;
    const nc = cc + dx;

    if (-5 <= nr && nr <= 5 && -5 <= nc && nc <= 5) {
      const cKey = String(cr) + String(cc);
      const nKey = String(nr) + String(nc);

      if (!visitedMap.has(cKey + nKey) && !visitedMap.has(nKey + cKey)) {
        answer += 1;

        visitedMap.set(cKey + nKey, true);
        visitedMap.set(nKey + cKey, true);
      }

      pos[0] = nr;
      pos[1] = nc;
    }
  });

  return answer;
}
