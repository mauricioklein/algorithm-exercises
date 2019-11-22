# Course Pre-requisites

This problem was asked by Google.

## Description

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. 

Return a valid ordering in which we can complete the courses. 

If no such ordering exists, return NULL.

## Example

```
Input:
{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

Output: ['CSC100', 'CSC200', 'CSC300']
```
