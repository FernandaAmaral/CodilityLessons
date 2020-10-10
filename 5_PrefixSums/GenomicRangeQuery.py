# Find the minimal nucleotide from a range of sequence DNA.

def solution(S, P, Q):
    M = len(P)
    result = [0] * M

    timeline = {
        'A': [0] * len(S),
        'C': [0] * len(S),
        'G': [0] * len(S),
        'T': [0] * len(S)
    }

    impact = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }

    timeline[S[0]][0] = 1

    for i in range(1, len(S)):
        for gene in timeline.keys():
            if(S[i] == gene):
                timeline[gene][i] = timeline[gene][i - 1] + 1
            else:
                timeline[gene][i] = timeline[gene][i - 1]

    for K in range(0, M):
        for gene in timeline.keys():
            if(Q[K] == P[K]):
                result[K] = impact[S[P[K]]]
                break
            if(timeline[gene][Q[K]] - timeline[gene][P[K]]):
                result[K] = impact[gene]
                break
            if(P[K] == 0 and timeline[gene][0]):
                result[K] = impact[gene]
                break
            if(P[K] != 0 and timeline[gene][P[K]] - timeline[gene][P[K]-1]):
                result[K] = impact[gene]
                break

    return result


S = 'ACGGT'
P = [0, 0, 3]
Q = [0, 1, 4]
print(solution(S, P, Q))
