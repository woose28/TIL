function solution(n, wires) {
  var answer = Infinity;

  const graph = wires.reduce((acc, wire) => {
    const [v1, v2] = wire;

    acc.has(v1) ? acc.get(v1).push(v2) : acc.set(v1, [v2]);
    acc.has(v2) ? acc.get(v2).push(v1) : acc.set(v2, [v1]);

    return acc;
  }, new Map());

  wires.forEach((wire) => {
    const [v1, v2] = wire;
    const visited = new Array(n).fill(false);
    visited[0] = true;

    const stack = [1];

    while (stack.length) {
      const cv = stack.pop();

      for (const nv of graph.get(cv)) {
        if ((cv === v1 && nv === v2) || (cv === v2 && nv === v1)) {
          continue;
        }

        if (!visited[nv - 1]) {
          visited[nv - 1] = true;
          stack.push(nv);
        }
      }
    }

    const curVisitedCount = visited.reduce(
      (acc, isVisited) => (isVisited ? acc + 1 : acc),
      0
    );

    answer = Math.min(answer, Math.abs(n - curVisitedCount - curVisitedCount));
  });

  return answer;
}
