'''
    제출 언어: Python3
    시간: 6304ms

    병합정렬 이용
'''
import sys

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    arr_l = arr[left: mid+1]
    arr_r = arr[mid+1: right+1]

    i, j, k = 0 , 0, left
    left_length, right_length = len(arr_l), len(arr_r)

    while i < left_length and j < right_length:
        if arr_l[i] >= arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        
        else:
            arr[k] = arr_r[j]
            j += 1

        k += 1

    while i < left_length:
        arr[k] = arr_l[i]

        k += 1
        i += 1

    while j < right_length:
        arr[k] = arr_r[j]

        k += 1
        j += 1
    


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    num_list = [ int(sys.stdin.readline().strip()) for _ in range(N) ]

    mergeSort(num_list, 0, N-1)

    for num in num_list:
        print(num)
    