def push_dominoes(dominoes):
  """
  Time complexity: O(n)
  Space complexity: O(n)
  """
  N = len(dominoes)
  forces = [0] * N

  # Forces from left to right
  f = 0
  for i in range(N):
    f = N if dominoes[i] == 'R' and f == 0 else \
        0 if dominoes[i] == 'L'            else \
        max(f - 1, 0)

    forces[i] += f

  # Forces from right to left:
  f = 0
  for i in range(N - 1, -1, -1):
    f = N if dominoes[i] == 'L' and f == 0 else \
        0 if dominoes[i] == 'R'            else \
        max(f - 1, 0)

    forces[i] -= f

  # Convert the forces into falling directions
  for i in range(N):
    forces[i] = 'R' if forces[i] > 0 else \
                'L' if forces[i] < 0 else \
                '.'

  return ''.join(forces)
