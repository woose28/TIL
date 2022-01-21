'''
    제출 언어: Python3
    시간: 2320ms
'''
import sys

def binary_search(target, left_idx):
    global A

    left = left_idx
    right = A-1

    while left <= right:
        mid = (left + right) // 2

        if target >= set_a[mid]:
            left = mid + 1

        else:
            right = mid - 1
    
    return right
            
if __name__ == "__main__":
    A, B = list(map(int, sys.stdin.readline().strip().split()))

    set_a = list(map(int, sys.stdin.readline().strip().split()))
    set_b = list(map(int, sys.stdin.readline().strip().split()))

    set_a.sort()
    set_b.sort()

    left_idx = 0

    answer_list = []
    
    for target in set_b:
        pos = binary_search(target, left_idx)

        if target == set_a[pos]:
            answer_list.extend(set_a[left_idx: pos])
    
        else:
            answer_list.extend(set_a[left_idx: pos+1])

        left_idx = pos+1    
    
    if left_idx < A:
        answer_list.extend(set_a[left_idx:])

    print(len(answer_list))

    if len(answer_list) > 0:
        print(' '.join(list(map(str, answer_list))))
    