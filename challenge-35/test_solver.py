import unittest
from solver import count_rectangles

class TestSolver(unittest.TestCase):
  def test_count_rectangles(self):
    points = [
      (1,3), (1,4), (2,3), (2,4)
    ]

    self.assertEqual(count_rectangles(points), 1)

  def test_count_multiple_rectangles(self):
    points = [
      (1,3), (1,4), (2,3), (2,4),
      (2,1), (2,2), (3,1), (3,2)
    ]
    
    self.assertEqual(count_rectangles(points), 2)

  def test_count_multiple_paralel_rectangles(self):
    points = [
      (1,3), (1,4), (2,3), (2,4), (3,3), (3,4), (4,3), (4,4)
    ]
    
    self.assertEqual(count_rectangles(points), 4)

if __name__ == "__main__":
    unittest.main()
