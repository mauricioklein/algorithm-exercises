import unittest
from solver import free_slots

class TestSolver(unittest.TestCase):
  def test_free_slots(self):
    window = (1,35)

    fn = lambda a, b: free_slots(a, b, window)

    self.assertEqual(fn([        ], [(10, 30)]), [(1,10), (30,35)])
    self.assertEqual(fn([(10, 30)], [        ]), [(1,10), (30,35)])
    self.assertEqual(fn([        ], [        ]), [window])

    cal_a = [(2,5), (10,14), (19,20), (27,30)]
    cal_b = [(3,5), (12,15), (18,21), (23,24)]
    exp   = [(1,2), (5,10), (15,18), (21,23), (24,27), (30,35)]
    self.assertEqual(fn(cal_a, cal_b), exp)

if __name__ == "__main__":
    unittest.main()
