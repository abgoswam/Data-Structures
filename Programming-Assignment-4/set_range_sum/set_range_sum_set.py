# python3

from sys import stdin

_set = set()

def insert(x):
    # print(">>>> Insert")
    _set.add(x)
    # for item in _set:
    #     print("---{0}---".format(item))

def erase(x):
    # print(">>>> Erase")
    if x in _set:
        _set.remove(x)

def search(x):
    # print(">>>> Search")
    return True if x in _set else False


def sum(fr, to):
    # print(">>>> Sum")
    ans = 0
    for item in _set:
        if fr <= item <= to:
            # print("-- {0} --".format(item))
            ans += item

    return ans


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
