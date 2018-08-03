# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight;

    def compute_height_fast(self):
        h = {}
        for i in range(self.n):
            h[i] = self.get_height(i, h)

        return max(h.items(), key=lambda x: x[1])[1]

    def get_height(self, i, h):
        if i in h:
            return h[i]

        if self.parent[i] == -1:
            return 1
        else:
            return self.get_height(self.parent[i], h) + 1


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(tree.compute_height_fast())


threading.Thread(target=main).start()
