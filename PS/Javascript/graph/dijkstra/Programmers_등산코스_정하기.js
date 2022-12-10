function calculateIntensity(intensities, graph, gates) {
  const que = gates.map((gate) => [gate, 0]);

  while (que.length) {
    const [cn, ci] = que.shift();

    if (intensities[cn] < ci) {
      continue;
    }

    for (const [nn, ni] of graph[cn]) {
      const maxI = Math.max(ci, ni);

      if (intensities[nn] > maxI) {
        intensities[nn] = maxI;
        que.push([nn, maxI]);
      }
    }
  }
}

function solution(n, paths, gates, summits) {
  var answer = [n + 1, Infinity];

  summits.sort((a, b) => a - b);

  const graph = {};

  new Array(n).fill(0).forEach((_, index) => {
    graph[index + 1] = [];
  });

  paths.forEach((path) => {
    const [i, j, w] = path;

    if (gates.includes(i)) {
      if (!gates.includes(j)) {
        graph[i].push([j, w]);
      }
      return;
    } else if (summits.includes(i)) {
      if (!summits.includes(j)) {
        graph[j].push([i, w]);
      }
      return;
    } else if (gates.includes(j)) {
      graph[j].push([i, w]);
      return;
    } else if (summits.includes(j)) {
      graph[i].push([j, w]);
      return;
    }

    graph[i].push([j, w]);
    graph[j].push([i, w]);
  });

  const intensities = new Array(n + 1).fill(Infinity);

  gates.forEach((gate) => {
    intensities[gate] = 0;
  });

  calculateIntensity(intensities, graph, gates);

  answer = summits.reduce(
    (acc, cur) => (acc[1] > intensities[cur] ? [cur, intensities[cur]] : acc),
    [n + 1, Infinity]
  );

  return answer;
}
