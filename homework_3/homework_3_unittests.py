import unittest
from homework_3_task1 import data_change_type_2



class TestCalculator(unittest.TestCase):

  def test_task1_str(self):
    self.assertEqual(data_change_type_2(str, '5','6'), ('5', '6'))
    self.assertEqual(data_change_type_2(str, 5,'6'), ('5', '6'))
    self.assertEqual(data_change_type_2(int, 5,'6'), (5, 6))
    self.assertEqual(data_change_type_2(float, 5,'6'), (5.0,6.0))
    self.assertEqual(data_change_type_2(list, 5,'6'), ([5, '6'],))
    self.assertEqual(data_change_type_2(tuple, 5,'6'), ((5, '6'),))
    self.assertEqual(data_change_type_2(str, 5,'6', 9.88), ('5', '6', '9.88'))
    self.assertEqual(data_change_type_2(int, 5,'6', 9.88), (5, 6, 9))
  



if __name__ == "__main__":
  unittest.main()