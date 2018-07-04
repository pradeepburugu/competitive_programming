import unittest


def isMatchingPair(character1,character2):
       if (character1 == '(' and  character2 == ')'):
         return True
       elif (character1 == '{' and character2 == '}'):
         return True
       elif (character1 == '[' and character2 == ']'):
         return True
       else:
         return False





def is_valid(exp):
       stack=[]
       for i in range(len(exp)):
           
          if (exp[i] == '{' or exp[i] == '(' or exp[i] == '['):
              stack.append(exp[i])
          if (exp[i] == '}' or exp[i] == ')' or exp[i] == ']'):
              if not stack:
                   return False
              elif (isMatchingPair(stack.pop(), exp[i]) ==False ):
                  return False
     
       if not stack:
           return True
       else:
           return False



















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)