# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTrav(self, node_id):
        if self.left[node_id] != -1:
            self.inOrderTrav(self.left[node_id])

        self.result.append(self.key[node_id])

        if self.right[node_id] != -1:
            self.inOrderTrav(self.right[node_id])

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inOrderTrav(0)
        return self.result

    def preOrderTrav(self, node_id):
        self.result.append(self.key[node_id])

        if self.left[node_id] != -1:
            self.preOrderTrav(self.left[node_id])

        if self.right[node_id] != -1:
            self.preOrderTrav(self.right[node_id])

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderTrav(0)
        return self.result

    def postOrderTrav(self, node_id):
        if self.left[node_id] != -1:
            self.postOrderTrav(self.left[node_id])

        if self.right[node_id] != -1:
            self.postOrderTrav(self.right[node_id])

        self.result.append(self.key[node_id])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postOrderTrav(0)
        return self.result


# if __name__ == '__main__':
def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
