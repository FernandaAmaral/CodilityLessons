# Count the number of passing cars on the road.

EAST = 0
WEST = 1


def solution(A):
    n_east = 0
    counter = 0

    for direction in A:
        if(direction == EAST):
            n_east += 1
        else:
            counter += n_east

        if counter > 1000000000:
            return -1

    return counter


A = [0, 1, 0, 1, 1]
print(solution(A))
