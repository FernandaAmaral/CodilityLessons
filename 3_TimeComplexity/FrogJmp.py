# Count minimal number of jumps from position X to Y.

def solution(X, Y, D):
    result = (Y-X)/D
    return int(result) + (not result.is_integer())


X = 10
Y = 85
D = 30
print(solution(X, Y, D))
