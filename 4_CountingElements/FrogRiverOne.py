# Find the earliest time when a frog can jump to the other side of a river.

def solution(X, A):
    leaves = [False] * X
    min_time = 0

    for time in range(0, len(A)):
        if(not leaves[A[time] - 1]):
            min_time = time
            leaves[A[time] - 1] = True

    if(False in leaves):
        return -1
    return min_time


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))
