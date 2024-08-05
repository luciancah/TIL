from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    
    for c in clothes:
        d[c[1]].append(c[0])
    
    d = list(d.items())
    answer = 1
    for i in d:
        answer *= (len(i[1])+1)
    answer -= 1
        
    
    return answer
