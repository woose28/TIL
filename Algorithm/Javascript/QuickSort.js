const data = [100, 4, 3, 82, 57, 63, 24];

function quickSort(arr, start, end) {
  if (start < end) {
    const pivot = partition(arr, start, end);

    quickSort(arr, start, pivot - 1);
    quickSort(arr, pivot + 1, end);
  }
}

function partition(arr, start, end) {
  let pivot = start;

  for (let i = start; i < end; i++) {
    if (arr[i] <= arr[end]) {
      const temp = arr[pivot];
      arr[pivot++] = arr[i];
      arr[i] = temp;

      continue;
    }
  }

  const temp = arr[end];
  arr[end] = arr[pivot];
  arr[pivot] = temp;

  return pivot;
}

quickSort(data, 0, data.length - 1);

console.log(data);
