# Determine whether a given string of parentheses (multiple types) is properly nested.

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

    char_dict = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    close_chars = [")", "}", "]"]
    open_chars = ["(", "{", "["]

    for char in A:
        if char in open_chars:
            push(char)
        if char in close_chars:
            if size == 0:
                return 0
            if stack[size - 1] == char_dict[char]:
                pop()
            else:
                return 0

    if size == 0:
        return 1
    return 0


A = "{[()()]}"
print(solution(A))
