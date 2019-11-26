PICKUP  = 'pickup'
DROPOFF = 'dropoff'

#
# Time  complexity: O(n*log(n)) (due the sorting)
# Space complexity: O(1)
#
def active_time(events):
  # sort the events by timestamp
  events.sort(key=lambda event: event[1])

  active_deliveries = 0
  start_timestamp = 0
  acc_active_time = 0

  for event in events:
    _, timestamp, action = event

    if action == PICKUP:
      active_deliveries += 1

      if active_deliveries == 1:
        start_timestamp = timestamp
    elif action == DROPOFF:
      active_deliveries -= 1

      if active_deliveries == 0:
        acc_active_time += (timestamp - start_timestamp)

  return acc_active_time
