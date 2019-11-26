#
# Time  complexity: O(n)
# Space complexity: O(1)
#
def buy_and_sell(prices):
  min_price  = float('inf')
  max_profit = 0

  for price in prices:
    min_price  = min(min_price , price            )
    max_profit = max(max_profit, price - min_price)

  return max_profit
