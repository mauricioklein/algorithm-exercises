# Flood fill

## Description

Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent (excluding diagonally adjacent) same colored pixels with the given color K.

## Example

```
Input:
[
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 2, 2, 0],
  [1, 1, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1]
]

x = 4, y = 4, k = 3

Output:
[
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1], 
  [1, 3, 3, 3, 3, 0, 1, 0],
  [1, 1, 1, 3, 3, 0, 1, 0],
  [1, 1, 1, 3, 3, 3, 3, 0],
  [1, 1, 1, 1, 1, 3, 1, 1],
  [1, 1, 1, 1, 1, 3, 3, 1]
]
```
