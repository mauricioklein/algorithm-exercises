# Sudoku solver

## Description

Given a partially filled 9×9 2D array `grid[9][9]`, the goal is to assign digits (from 1 to 9) to the empty cells (denoted by the number `zero`) so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.

## Example
```
Input:
  [
    [3, 0, 6, 5, 0, 8, 4, 9, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
  ]

Output: a valid Sudoku board
```
