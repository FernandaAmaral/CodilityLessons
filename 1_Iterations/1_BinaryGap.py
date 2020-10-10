# Find longest sequence of zeros in binary representation of an integer.

def solution(N):
    bits = bin(N).split('b')[1]     # Binary string
    bit_sum = 0                     # Sum of zeros
    maximum = 0                     # Maximum gap found
    find_one = False                # Found at least one bit=1

    for bit in bits:
        if(bit == '0' and find_one):
            bit_sum += 1
        else:
            if(find_one and bit_sum > maximum):
                maximum = bit_sum
            bit_sum = 0
            find_one = True

    return maximum


print(solution(561892))
