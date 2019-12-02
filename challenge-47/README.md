# Closest coin

This problem was asked by Google.

## Description

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

## Example
```
Input:
  coins: [(0,4), (1,0), (2,0), (2,4), (3,2)] # Pair (row, column)
  your position: (0,2)

Output: (0,4)
```
