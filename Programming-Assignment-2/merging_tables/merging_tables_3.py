# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

rank = [1] * n
parent = list(range(0, n))

def getParent(table):
    # find parent and compress path
    if parent[table] != table:
        p = getParent(parent[table])
        parent[table] = p

    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    parent[realSource] = realDestination
    lines[realDestination] += lines[realSource]
    if rank[realSource] == rank[realDestination]:
        rank[realDestination] += 1

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    # print(lines)
    print(max(lines))
    
