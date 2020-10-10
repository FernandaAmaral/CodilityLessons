# Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    if(A == B):
        return (1 if A % K == 0 else 0)

    if(K > A and A != 0):
        A = K

    if(A % K == 0):
        A -= 1

    return int((B - A) / K) + ((B - A) % K > 0)


A = 101
B = 123456789
K = 10000
print(solution(A, B, K))
