# 들어가며
C++, Python 같은 언어와 다르게 Javascript에서는 기본적인 자료구조가 부실하다.
따라서 PS 할 때 자료 구조를 이용하고 싶다면 직접 구현해야 한다.
해당 게시글에서 Javascript로 구현한 자료구조 코드를 정리하려 한다.

<br />

# 자료 구조 구현 코드

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
