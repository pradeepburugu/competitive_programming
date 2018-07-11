import unittest


def find_repeat(the_list):
    a=1
    b=len(the_list)-1
    while a<b:
        midpoint=a+((b-a)/2)
        lowerrange_a, lowerrange_b=a,midpoint
        upperrange_a,upperrange_b= midpoint+1,b
        c=0
        for i in the_list:
            if i>=lowerrange_a and i<=lowerrange_b:
                c+= 1
        d=(lowerrange_b-lowerrange_a+1)
        if c>d:
            
            a,b=lowerrange_a,lowerrange_b
        else:
            
            a,b=upperrange_a,upperrange_b

    
    return a
















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)