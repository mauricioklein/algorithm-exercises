import unittest
from solver import active_time

class TestSolver(unittest.TestCase):
  def test_active_time(self):
    events = [
      (1,  1, 'pickup' ),
      (1,  5, 'dropoff'),
      (2,  7, 'pickup' ),
      (3, 10, 'pickup' ),
      (3, 12, 'dropoff'),
      (2, 15, 'dropoff')
    ]
    expected_output = 12

    self.assertEqual(active_time(events), expected_output)

if __name__ == "__main__":
    unittest.main()
