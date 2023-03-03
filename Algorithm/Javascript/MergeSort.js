const data = [100, 4, 3, 82, 57, 63, 24];

function mergeSort(arr, start, end) {
  if (start < end) {
    const mid = Number.parseInt((start + end) / 2);

    mergeSort(arr, start, mid);
    mergeSort(arr, mid + 1, end);

    merge(arr, start, mid, end);
  }
}

function merge(arr, start, mid, end) {
  const tempArr = new Array(end - start + 1);
  let currentIndex = 0;

  let frontIndex = start;
  let endIndex = mid + 1;

  while (frontIndex <= mid && endIndex <= end) {
    if (arr[frontIndex] < arr[endIndex]) {
      tempArr[currentIndex++] = arr[frontIndex++];
      continue;
    }

    tempArr[currentIndex++] = arr[endIndex++];
  }

  while (frontIndex <= mid) {
    tempArr[currentIndex++] = arr[frontIndex++];
  }

  while (endIndex <= end) {
    tempArr[currentIndex++] = arr[endIndex++];
  }

  tempArr.forEach((value, index) => {
    arr[start + index] = value;
  });
}

mergeSort(data, 0, data.length - 1);

console.log(data);
