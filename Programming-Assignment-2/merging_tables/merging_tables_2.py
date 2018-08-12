# python3

import sys

def getRoot(table):
    # while table != root[table]:
    #     table = root[table]
    # return table

    if table == parent[table]:
        return table

    parent[table] = getRoot(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getRoot(destination), getRoot(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if rank[realSource] <= rank[realDestination]:
        parent[realSource] = realDestination
        root[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1
    else:
        parent[realDestination] = realSource
        root[realSource] = realDestination
        disobey[realSource] = 1
        lines[realDestination] += lines[realSource]

    return True


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    parent = list(range(0, n))
    root = list(range(0, n))
    disobey = [0] * n
    rank = [1] * n

    data = list(map(int, sys.stdin.read().split()))
    t_destinations = data[0::2]
    t_sources = data[1::2]
    t = list(zip(t_destinations, t_sources))

    for item in t:
        merge(item[0]-1, item[1]-1)
        # print(lines)
        print(max(lines))

