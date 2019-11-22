# Validate BST

## Description

Given a binary tree, determine if it's a valid binary search tree (BST)

Assume a BST is defined as follow:

- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also by BSTs

## Example

```
        5
       / \
      /   \
     1     4
          / \
         3   6
 
Output: False (3 is less than 5) 
```
