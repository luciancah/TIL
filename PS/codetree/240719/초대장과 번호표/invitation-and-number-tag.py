import sys

sys.setrecursionlimit(10**5)


n, g = map(int, input().split())
groups = [list(map(int, input().split()))[1:] for _ in range(g)]

res = set()
res.add(1)

def add_user(groups, res):
    for gr in groups:
        subgroup_length = len(gr)
        count = 0
        cache = set()
        for i in range(subgroup_length):
            if gr[i] not in res:
                cache.add(gr[i])
            if len(cache) >= 2:
                break
        
        if len(cache) == 1:
            res.add(cache.pop())
            # print(res)
            add_user(groups,res)
            return
    return    

    
add_user(groups,res)

print(len(res))