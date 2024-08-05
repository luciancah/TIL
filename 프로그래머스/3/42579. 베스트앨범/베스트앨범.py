from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(int)
    gs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        d[g] += p
        gs[g].append([i, p])
    
    d = list(d.items())
    d.sort(key=lambda x: -x[1])
    
    for g in d:
        answer += [x[0] for x in sorted(gs[g[0]], key=lambda x: -x[1])[:2]]
    
    return answer
