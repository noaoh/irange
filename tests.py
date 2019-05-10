import unittest
import pdb
from irange import irange


class ZeroArgumentsTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(TypeError, irange)


class TooManyArgumentsTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(TypeError, irange, 1, 2, 3, 4)
        self.assertRaises(TypeError, irange, 1, 2, 3, 4, 5)


class WrongTypeArgumentTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(TypeError, irange, "1", 7, 3)
        self.assertRaises(TypeError, irange, 1.0, 7, 3)
        self.assertRaises(TypeError, irange, True, 7, 3)
        self.assertRaises(TypeError, irange, None, 7, 3)


class StepIsZeroTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, irange, 1, 5, 0)


def main():
    unittest.main()


if __name__ == "__main__":
    main()

