# Find the minimal average of any slice containing at least two elements.

def average2(A):
    avg = [0] * (len(A) - 1)
    for i in range(0, len(A) - 1):
        avg[i] = (A[i] + A[i+1])/2
    return avg


def average3(A):
    avg = [0] * (len(A) - 2)
    for i in range(0, len(A) - 2):
        avg[i] = (A[i] + A[i+1] + A[i+2])/3
    return avg


def solution(A):
    avg2 = average2(A)
    avg3 = average3(A)

    # If the array contains two numbers, the only
    # possible index is 0
    if(len(A) < 3):
        return 0

    # If both lists contains the same min value,
    # return the one with the lowest index
    if(min(avg2) == min(avg3)):
        index2 = avg2.index(min(avg2))
        index3 = avg3.index(min(avg3))
        if(index2 <= index3):
            return index2
        return index3

    # Otherwise, return the lowest average
    if(min(avg2) < min(avg3)):
        return avg2.index(min(avg2))
    return avg3.index(min(avg3))


A = [-1, -1, 0, 0, -1, -1, -1]
print(solution(A))
