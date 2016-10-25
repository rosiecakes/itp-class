def wrong_value(input):
    if isinstance(input, int):
        print('{} is a number'.format(input))
    else:
        raise ValueError('Please input a number!')



import unittest


class RaiseValueErrorTest(unittest.TestCase):
    def value_error_test(self):
        self.assertRaises(ValueError, wrong_value('string'))
        self.assertEqual(wrong_value(3), '3 is a number')

if __name__ == '__main__':
    unittest.main()
