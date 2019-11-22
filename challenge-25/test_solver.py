import unittest
from solver import push_dominoes

class TestSolver(unittest.TestCase):
  def test_push_dominoes(self):
    self.assertEqual(push_dominoes("..R...L..R."), "..RR.LL..RR")
    self.assertEqual(push_dominoes("R..LL.."    ), "RR.LL.."    )
    self.assertEqual(push_dominoes("R...L"      ), "RR.LL"      )
    self.assertEqual(push_dominoes("R...."      ), "RRRRR"      )
    self.assertEqual(push_dominoes("....L"      ), "LLLLL"      )
    self.assertEqual(push_dominoes("....R"      ), "....R"      )
    self.assertEqual(push_dominoes("L...."      ), "L...."      )
    self.assertEqual(push_dominoes("....."      ), "....."      )
    self.assertEqual(push_dominoes(""           ), ""           )

if __name__ == "__main__":
    unittest.main()
