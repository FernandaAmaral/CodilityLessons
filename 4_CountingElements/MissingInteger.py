# Find the smallest positive integer that does not occur in a given sequence.

def solution(A):
    smallest = 1
    A = sorted(A)

    for x in A:
        if(x == smallest):
            smallest += 1

    return smallest


A = [1, 3, 6, 4, 1, 2]
print(solution(A))
