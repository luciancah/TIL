from collections import defaultdict

def solution(participant, completion):

    d = defaultdict(int)
    
    for p in participant:
        d[p] += 1
    
    for c in completion:
        d[c] -= 1
    
    d = sorted(list(d.items()), key=lambda x: -x[1])


    
    
    return d[0][0]