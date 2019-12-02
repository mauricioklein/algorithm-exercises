def closest_coin(coins, p):
  if not coins:
    return None

  closest_dist = float('inf')
  closest_point = None

  for coin in coins:
    dist = distance(p, coin)

    if dist < closest_dist:
      closest_dist = dist
      closest_point = coin

  return closest_point

def distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2

  return abs(x1 - x2) + abs(y1 - y2)
