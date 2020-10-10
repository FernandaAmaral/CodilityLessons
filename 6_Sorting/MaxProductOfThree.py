# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

POSITIVE = 1
NEGATIVE = -1


def solution(A):
    A_abs = [abs(x) for x in A]
    A_index = sorted(range(len(A)), key=lambda k: A_abs[k], reverse=True)
    A_sorted = [A_abs[i] for i in A_index]
    sign = [POSITIVE if A[x] > 0 else NEGATIVE for x in A_index]

    # If the multiplication of the three first numbers is positive
    if (sign[0] * sign[1] * sign[2] == POSITIVE):
        return A_sorted[0] * A_sorted[1] * A_sorted[2]

    # If there are only negative numbers in the array
    if (POSITIVE not in sign):
        return - A_sorted[-1] * A_sorted[-2] * A_sorted[-3]

    # If the three first elements are negative
    # Replace the last with the next positive one
    if (POSITIVE not in sign[0:3]):
        next_positive = sign[3:].index(POSITIVE) + 3
        return A_sorted[0] * A_sorted[1] * A_sorted[next_positive]

    # If there is a single negative in first three elements
    neg = sign[0:3].index(NEGATIVE)

    # Option 1: Replace the negative with the next positive number
    opt1 = 0
    if (POSITIVE in sign[3:]):
        opt1 = 1
        idx = sign[3:].index(POSITIVE)

        for i in range(3):
            if (i != neg):
                opt1 *= A_sorted[i]
            else:
                opt1 *= A_sorted[idx + 3]

    # Option 2: Replace the last positive with the next negative number
    opt2 = 0
    if (NEGATIVE in sign[3:]):
        idx = sign[3:].index(NEGATIVE)
        if(sign[2] is POSITIVE):
            opt2 = A_sorted[0] * A_sorted[1] * A_sorted[idx + 3]
        else:
            opt2 = A_sorted[0] * A_sorted[2] * A_sorted[idx + 3]

    if (opt2 > opt1):
        return opt2
    return opt1


A = [-3, 1, 2, -2, 5, 6]
print(solution(A))
