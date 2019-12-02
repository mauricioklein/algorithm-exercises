import unittest
from solver import create_balanced_bst

class TestSolver(unittest.TestCase):
  def test_create_balanced_bst(self):
    self.assertEqual(str(create_balanced_bst([1,2,3,4,5,6,7])), "4261357")
    self.assertEqual(str(create_balanced_bst([1,2,3        ])),     "213")
    self.assertEqual(str(create_balanced_bst([1,2,3,4      ])),    "3241")
    self.assertEqual(str(create_balanced_bst([1            ])),       "1")

if __name__ == "__main__":
    unittest.main()
