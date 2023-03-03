const data = [100, 4, 3, 82, 57, 63, 24];

function bubbleSort(data) {
  const N = data.length;

  for (let i = 0; i < N; i++) {
    const lastIndex = N - i - 1;

    for (let j = 0; j < lastIndex; j++) {
      if (data[j] > data[j + 1]) {
        const temp = data[j];
        data[j] = data[j + 1];
        data[j + 1] = temp;
      }
    }
  }
}

bubbleSort(data);

console.log(data);
