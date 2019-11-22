import unittest
from solver import courses_to_take

class TestSolver(unittest.TestCase):
  def test_courses_to_take(self):
    self.assertEqual(
      courses_to_take({
        'CSC300': ['CSC100', 'CSC200'], 
        'CSC200': ['CSC100'], 
        'CSC100': []
      }),
      ['CSC100', 'CSC200', 'CSC300']
    )

    self.assertEqual(
      courses_to_take({
        'CSC400': ['CSC300', 'CSC200'], 
        'CSC300': ['CSC200'],
        'CSC200': ['CSC300', 'CSC100'],
        'CSC100': []
      }),
      None
    )

if __name__ == "__main__":
    unittest.main()
