import sys

def recursive(length):
    global N, M, num_list, selected

    if length == M:
        print(" ".join(map(str, selected)))
        return

    last_selected = 0

    for i in range(N):
        if not is_selected[i] and last_selected != num_list[i]:
            last_selected = num_list[i]
            is_selected[i] = True
            selected.append(num_list[i])
            recursive(length+1)
            selected.pop()
            is_selected[i] = False
    

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()
    
    is_selected = [ False ] * N
    selected = []

    recursive(0)

