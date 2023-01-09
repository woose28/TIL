function solution(bridge_length, weight, truck_weights) {
  var answer = 0;

  const trucks = [...truck_weights];

  answer = 1;
  const bridge = [[trucks.shift(), answer]];

  while (bridge.length !== 0) {
    answer += 1;

    if (answer - bridge[0][1] === bridge_length) {
      bridge.shift();
    }

    if (bridge.length < bridge_length) {
      bridgeWeight = bridge.reduce((acc, truck) => acc + truck[0], 0);

      if (bridgeWeight + trucks[0] <= weight && trucks.length > 0) {
        bridge.push([trucks.shift(), answer]);
      }
    }
  }

  return answer;
}
