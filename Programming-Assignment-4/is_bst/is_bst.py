#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def post_order_traversal(tree, node_index):
    node = tree[node_index]

    key = node[0]
    left_node_index = node[1]
    right_node_index = node[2]

    min_left = 2**31-1
    max_left = -2**31

    min_right = 2**31-1
    max_right = -2**31

    if left_node_index != -1:
        valid, min_left, max_left = post_order_traversal(tree, left_node_index)
        if not valid:
            return valid, min_left, max_left

    if right_node_index != -1:
        valid, min_right, max_right = post_order_traversal(tree, right_node_index)
        if not valid:
            return valid, min_right, max_right

    if max_left >= key or key >= min_right:
        return False, -1, -1

    # so we have verified  max_left < key < min_right. so BST condition is validated
    # need to send min, max of tree rooted at node
    _min = min(key, min_left)
    _max = max(key, max_right)
    return True, _min, _max


def IsBinarySearchTree(tree):
    # Implement correct algorithm here

    # for node in tree:
    #     print(node)

    if not tree:
        return True

    valid, _, _ = post_order_traversal(tree, 0)
    return valid


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    # print(tree)

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
