"""
  Time  complexity: O(n*m) (where n = length of "cal_a", m = length of "cal_b")
  Space complexity: O(n*m) (for the result array with free slots)
"""
def free_slots(cal_a, cal_b, time_window):
  busy = None
  free = []

  if not (cal_a or cal_b):
    """
    Both calendars empty = the entire time window is free
    """
    return [time_window]

  window_start, window_end = time_window

  while cal_a or cal_b:
    t = cal_b.pop(0) if not cal_a else \
        cal_a.pop(0) if not cal_b else \
        cal_a.pop(0) if cal_a[0] < cal_b[0] else \
        cal_b.pop(0)

    t_start, t_end = t

    if not busy:
      """
      First event:
      - Register a free slot between the time window begin and the first event start
      - Register the event as the first busy
      """
      free.append( (window_start, t_start) )
      busy = t
    else:
      busy_start, busy_end = busy

      if not overlap(busy, t):
        """
        Non-overlapping events = we have a free window between them
        """
        free.append( (busy_end, t_start) )

      busy = (
        min(busy_start, t_start), 
        max(busy_end,   t_end  )
      )

  """
  Check a free window between the end of the last event 
  and the time window end
  """
  busy_end = busy[1]
  if busy_end < window_end:
    free.append( (busy_end, window_end) )

  return free

"""
Check if t1 and t2 overlap
"""
def overlap(t1, t2):
  t1_start, t1_end = t1
  t2_start, t2_end = t2

  if t1_start <= t2_start:
    return t2_start <= t1_end
  else:
    return t2_end <= t1_start
