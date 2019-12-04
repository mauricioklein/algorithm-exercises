# Deepest Node in a Binary Tree

This problem was asked by Google.

## Description

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

## Example
```
#     a
#    / \
#   b   c
#  /
# d

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root)) # (d, 3)
```
