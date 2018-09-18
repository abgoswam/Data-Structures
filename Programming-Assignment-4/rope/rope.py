# python3

import sys

class Rope:
    def __init__(self, s):
        self.s = s
    def result(self):
        return self.s
    def process(self, i, j, k):
        # Write your code here
        substr = self.s[i:j+1]
        s1 = self.s[:i]
        s2 = self.s[j+1:]
        s_combine = s1 + s2

        a1 = s_combine[:k]
        a2 = s_combine[k:]
        self.s = a1 + substr + a2
        # print(self.s)


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
