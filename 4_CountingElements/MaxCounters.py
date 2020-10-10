# Calculate the values of counters after applying all alternating operations:
# increase counter by 1; set value of all counters to current maximum.

def solution(N, A):
    max_counter = 0
    add_counter = 0
    counter = N * [0]

    for X in A:
        if(X >= 1 and X <= N):
            if(counter[X-1] < add_counter):
                counter[X-1] = add_counter

            counter[X-1] += 1

            if(counter[X-1] > max_counter):
                max_counter = counter[X-1]

        if(X == N+1):
            add_counter = max_counter

    return [add_counter if x < add_counter else x for x in counter]


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
print(solution(N, A))
