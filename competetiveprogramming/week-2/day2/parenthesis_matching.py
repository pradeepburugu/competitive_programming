import unittest


def get_closing_paren(sentence, index):

    # Find the position of the matching closing parenthesis
    i = index
    end = len(sentence)
    count = 0
    while i < end:
        ch = sentence[i]
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
            if count == 0:
                return i
        i += 1
    if count!=0:
        raise Exception


















# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)

    def test_no_matching(self):
        # with self.assertRaises(Exception):
        we=get_closing_paren('(((()())', 2)
        expected=7
        self.assertEqual(we,expected)


unittest.main(verbosity=2)