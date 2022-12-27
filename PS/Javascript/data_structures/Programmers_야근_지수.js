class MaxHeap {
  constructor(initialData) {
    this.heap = [];

    if (Array.isArray(initialData)) {
      initialData.forEach((value) => {
        this.heapPush(value);
      });
    }
  }

  heapPush(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  heapPop() {
    const size = this.getSize();
    const maxValue = size === 0 ? 0 : this.heap[0];

    if (size === 1) {
      this.heap = [];
    } else if (size > 1) {
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
    }

    return maxValue;
  }

  getSize() {
    return this.heap.length;
  }

  heapifyUp() {
    let currentIndex = this.getSize() - 1;

    while (currentIndex > 0) {
      const parentIndex = this.getParentIndex(currentIndex);

      if (this.heap[parentIndex] > this.heap[currentIndex]) {
        break;
      }

      this.swap(currentIndex, parentIndex);
      currentIndex = parentIndex;
    }
  }

  heapifyDown() {
    let currentIndex = 0;
    const target = this.heap[currentIndex];
    const size = this.getSize();

    while (this.getLeftChildIndex(currentIndex) < size) {
      const leftChildIndex = this.getLeftChildIndex(currentIndex);
      const rightChildIndex = this.getRightChildIndex(currentIndex);

      const largerChildIndex =
        rightChildIndex < size &&
        this.heap[rightChildIndex] >= this.heap[leftChildIndex]
          ? rightChildIndex
          : leftChildIndex;

      if (this.heap[largerChildIndex] < target) {
        break;
      }

      this.swap(currentIndex, largerChildIndex);
      currentIndex = largerChildIndex;
    }
  }

  swap(someIndex, otherIndex) {
    const temp = this.heap[someIndex];
    this.heap[someIndex] = this.heap[otherIndex];
    this.heap[otherIndex] = temp;
  }

  getLeftChildIndex(parentIndex) {
    return parentIndex * 2 + 1;
  }

  getRightChildIndex(parentIndex) {
    return parentIndex * 2 + 2;
  }

  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }
}

function solution(n, works) {
  var answer = 0;

  const maxHeap = new MaxHeap(works);
  let curN = n;

  while (curN > 0) {
    const maxWork = maxHeap.heapPop();
    const nextWork = maxWork > 1 ? maxWork - 1 : 0;

    maxHeap.heapPush(nextWork);
    curN -= 1;
  }

  answer = maxHeap.heap.reduce((acc, curWork) => acc + curWork ** 2, 0);

  return answer;
}
