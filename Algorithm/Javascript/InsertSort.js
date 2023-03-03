const data = [100, 4, 3, 82, 57, 63, 24];

function insertSort(data) {
  const N = data.length;

  for (let i = 1; i < N; i++) {
    const currentNum = data[i];
    let j;

    for (j = i - 1; j >= 0; j--) {
      if (currentNum >= data[j]) {
        break;
      }

      data[j + 1] = data[j];
    }

    data[j + 1] = currentNum;
  }
}

insertSort(data);

console.log(data);
