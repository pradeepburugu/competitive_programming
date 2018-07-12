import unittest


  def find_duplicate(int_list):
    n = len(int_list) - 1
    position = n + 1
    for i in range(n):
        position = int_list[position - 1]
    remembered = position
    current = int_list[position - 1]  
    cycle = 1
    while current != remembered:
        current = int_list[current - 1]
        cycle += 1
    start = n + 1
    ahead = n + 1
    for i in range(cycle):
        ahead = int_list[ahead - 1]
    while start != ahead:
        start = int_list[start - 1]
        ahead = int_list[ahead - 1]
    return start


















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)