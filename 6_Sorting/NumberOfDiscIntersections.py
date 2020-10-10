# Compute the number of intersections in a sequence of discs.

def solution(A):
    N = len(A)          # Size of array
    counter = 0         # Number of intersections
    opened = 0          # Number of circles we are inside when looping

    # Handling empty array
    if(N == 0):
        return 0

    # Create array of objects with all points in x axis
    data = []
    for i in range(N):
        data.append(
            {
                "type": "start",
                "value": i - A[i],
                "index": i
            }
        )
        data.append(
            {
                "type": "end",
                "value": i + A[i],
                "index": i
            }
        )

    # Get index sorted from smallest to highest value
    index = sorted(range(len(data)), key=lambda k: data[k]['value'])

    # Auxiliar variables for counting tangent circles
    last_val = data[index[0]]['value'] - 1
    tangent_counter = 1

    for i in index:
        if data[i]['type'] == "start":
            counter += opened
            opened += 1
        else:
            opened -= 1

        # Handling tangent intersections
        if data[i]['type'] == "start" and data[i]['value'] == last_val:
            counter += tangent_counter
        if data[i]['type'] == "end":
            if data[i]['value'] == last_val:
                tangent_counter += 1
            else:
                last_val = data[i]['value']
                tangent_counter = 1

        # Handling maximum pairs exceed
        if counter > 10000000:
            return -1

    return counter


A = [1, 5, 8, 7, 8, 4, 8, 5, 0, 5]
# A = [1, 5, 2, 1, 4, 0]

print(solution(A))
