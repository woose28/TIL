const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const data = fs.readFileSync(filePath).toString().trim().split("\n");

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

const [N, ...operators] = data.map(Number);
const result = [];
const heap = new MaxHeap();

operators.forEach((operator) => {
  if (operator === 0) {
    const value = heap.heapPop();

    result.push(value);
    return;
  }

  heap.heapPush(operator);
});

console.log(result.join("\n"));
