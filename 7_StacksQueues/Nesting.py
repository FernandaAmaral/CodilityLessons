# Determine whether a given string of parentheses (single type) is properly nested.

stack = []
size = 0


def push(x):
    global size
    stack[size] = x
    size += 1


def pop():
    global size
    size -= 1
    return stack[size]


def solution(A):
    global stack, size
    stack = [None] * len(A)
    size = 0

    for char in A:
        if char == "(":
            push(char)
        if char == ")":
            if size == 0:
                return 0
            if stack[size - 1] == "(":
                pop()
            else:
                return 0

    if size == 0:
        return 1
    return 0


A = "(()(())())"
print(solution(A))
