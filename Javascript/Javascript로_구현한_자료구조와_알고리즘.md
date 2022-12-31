# 들어가며
C++, Python 같은 언어와 다르게 Javascript에서는 기본적인 자료구조가 부실하다.
따라서 PS 할 때 자료 구조를 이용하고 싶다면 직접 구현해야 한다.
자료 구조 이외에도 알고리즘 관련된 내장 함수가 제공되지 않는 경우가 있다.
해당 게시글에서 Javascript로 구현한 자료구조 및 알고리즘 코드를 정리하려 한다.

<br />

## 자료 구조 구현 코드

<details>
  <summary>최소 힙 코드</summary>
  
  ```javascript
  class MinHeap {
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
      const minValue = size === 0 ? 0 : this.heap[0];

      if (size === 1) {
        this.heap = [];
      } else if (size > 1) {
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
      }

      return minValue;
    }

    getSize() {
      return this.heap.length;
    }

    heapifyUp() {
      let currentIndex = this.getSize() - 1;

      while (currentIndex > 0) {
        const parentIndex = this.getParentIndex(currentIndex);

        if (this.heap[parentIndex] < this.heap[currentIndex]) {
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

        const smallerChildIndex =
          rightChildIndex < size &&
          this.heap[rightChildIndex] < this.heap[leftChildIndex]
            ? rightChildIndex
            : leftChildIndex;

        if (this.heap[smallerChildIndex] > target) {
          break;
        }

        this.swap(currentIndex, smallerChildIndex);
        currentIndex = smallerChildIndex;
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
  ```
</details>

<br />

<details>
  <summary>순열 코드</summary>
  1부터 N까지 M개의 숫자를 선택해서 순열을 만드는 코드

  ```javascript
  const answer = [];
  const [N, M] = data.split(" ").map(Number);

  const isSelected = new Array(N + 1).fill(false);

  function permutation(selected) {
    if (selected.length === M) {
      answer.push(selected.join(" "));
    }

    for (let i = 1; i <= N; i++) {
      if (!isSelected[i]) {
        isSelected[i] = true;
        selected.push(i);
        permutation(selected);
        selected.pop();
        isSelected[i] = false;
      }
    }
  }

  permutation([]);
  ```
</details>

<br />

<details>
  <summary>조합 코드</summary>
  1부터 N까지 M개의 숫자를 선택해서 조합을 만드는 코드

  ```javascript
  const answer = [];
  const [N, M] = data.split(" ").map(Number);

  function combination(lastIndex, selected) {
    if (selected.length === M) {
      answer.push(selected.join(" "));
      return;
    }

    for (let i = lastIndex + 1; i <= N; i++) {
      selected.push(i);

      combination(i, selected);

      selected.pop();
    }
  }

  combination(0, []);
  ```
</details>
