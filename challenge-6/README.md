# Serialize/Deserialize binary tree

This problem was asked by Google.

## Description

Given the root to a binary tree, implement serialize (root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

## Examples

Given the following Node class:

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
