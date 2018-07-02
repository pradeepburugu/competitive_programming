import unittest

in_stack=[]
out=[]
class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    

    def enqueue(self, item):
        in_stack.append(item)

    def dequeue(self):
        if(len(out)==0):
            while len(in_stack)>0:
                item=in_stack.pop()
                out.append(item)
            if len(out)==0:
                raise Exception
        return out.pop()


















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)