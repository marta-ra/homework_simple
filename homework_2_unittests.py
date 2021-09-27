import unittest
from homework_2_task1 import task1
from homework_2_task2 import task2


class TestCalculator(unittest.TestCase):

  def test_task1_str(self):
    self.assertEqual(task1('5','6'), '56')
  def test_task1_int(self):
    self.assertEqual(task1(5,6), 1)
    self.assertEqual(task1(11.5,6), 5.5)
  def test_task1_error(self):
    self.assertEqual(task1('5',6), None)
    self.assertEqual(task1(4, 25), None)
    self.assertEqual(task1(3.6, 25), None)
    self.assertEqual(task1(10, 2.7), None)
  

  def test_task2_tests(self):
    self.assertEqual(task2(5, 6, '+'), 11)
    self.assertEqual(task2(10, 6, '*'), 60)
    self.assertEqual(task2(21, 3, '/'), 7)
    self.assertEqual(task2(21,3, '-'), 18)
    self.assertEqual(task2(28, 6, '+'), 'Введите число от 3 до 23')
    self.assertEqual(task2(0, 15, '*'), 'Введите число от 3 до 23')
    self.assertEqual(task2(25, 20, '*'), 'Введите число от 3 до 23')


if __name__ == "__main__":
  unittest.main()