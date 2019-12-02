# Median of window

This problem was asked by Microsoft.

## Description

Given an array of numbers "arr" and a window of size "k", return an array with the median of each window of size "k" starting from the left and moving right by one position each time.

Recall that the median of an even-sized list is the average of the two middle numbers.

## Example
```
Input:
  arr: [-1, 5, 13, 8, 2, 3, 3, 1]

Output:
  [5, 8, 8, 3, 3, 3]
  # 5 <- median of [-1, 5, 13]
  # 8 <- median of [5, 13, 8]
  # 8 <- median of [13, 8, 2]
  # 3 <- median of [8, 2, 3]
  # 3 <- median of [2, 3, 3]
  # 3 <- median of [3, 3, 1]
```
