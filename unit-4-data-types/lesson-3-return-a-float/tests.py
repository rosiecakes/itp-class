import unittest


class ReturnAFloatTest(unittest.TestCase):
    def test_return_a_float(self):
        self.assertEqual(return_float(30), 50.0)
        self.assertEqual(return_float(13), 21.7)
        self.assertEqual(return_float(42), 70.0)
        self.assertEqual(return_float(60), 100.0)
