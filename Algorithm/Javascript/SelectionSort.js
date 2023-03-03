const data = [100, 4, 3, 82, 57, 63, 24];

function selectionSort(data) {
  const N = data.length;

  for (let i = 0; i < N; i++) {
    const lastIndex = N - i - 1;
    let maxIndex = 0;

    for (let j = 1; j <= lastIndex; j++) {
      if (data[maxIndex] < data[j]) {
        maxIndex = j;
      }
    }

    const temp = data[maxIndex];
    data[maxIndex] = data[lastIndex];
    data[lastIndex] = temp;
  }
}

selectionSort(data);

console.log(data);
