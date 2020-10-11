# N voracious fish are moving along a river. Calculate how many fish are alive.

UPSTREAM = 0
DOWNSTREAM = 1
stack = []
size = 0


def push(fish_size, fish_direction):
    global size
    stack[size] = {
        "size": fish_size,
        "direction": fish_direction
    }
    size += 1


def pop():
    global size
    size -= 1
    return stack[size]


def found_fish(fish_size, fish_direction):
    global stack, size

    # If there is no fish in stack, add this fish
    if not size:
        push(fish_size, fish_direction)
        return 0

    # Add fish to stack if previous fish is in the same direction
    if(stack[size-1]['direction'] == fish_direction):
        push(fish_size, fish_direction)
        return 0

    # If previous fish is going upstream, add fish to stack
    if(stack[size-1]['direction'] == UPSTREAM):
        push(fish_size, fish_direction)
        return 0

    # If previous fish is going downstream and this is bigger, remove previous
    if(stack[size-1]['size'] < fish_size):
        pop()
        return 1

    # If this fish is smaller and in opposite direction, ignore it
    return 0


def solution(A, B):
    N = len(A)
    global stack, size
    stack = [None] * N

    for i in range(N):
        while(found_fish(A[i], B[i])):
            pass
    return size

                

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

print(solution(A, B))
