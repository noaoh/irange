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


class StartUpToEndTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(list(irange(5)), [0, 1, 2, 3, 4, 5])
        self.assertEqual(list(irange(0, 4)), [0, 1, 2, 3, 4])
        self.assertEqual(list(irange(0, 6, 2)), [0, 2, 4, 6])
        self.assertEqual(list(irange(1, 10, 4)), [1, 5, 9])
        self.assertEqual(list(irange(-1, 3)), [-1, 0, 1, 2, 3])
        self.assertEqual(list(irange(-5, 0, 2)), [-5, -3, -1])


class StartDownToEndTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(list(irange(4, 0, -1)), [4, 3, 2, 1, 0])
        self.assertEqual(list(irange(10, 1, -4)), [10, 6, 2])
        self.assertEqual(list(irange(5, -2, -1)), [5, 4, 3, 2, 1, 0, -1, -2])
        self.assertEqual(list(irange(5, 0, -2)), [5, 3, 1])


class NoValuesTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(list(irange(5, 5)), [])
        self.assertEqual(list(irange(6, 2)), [])
        self.assertEqual(list(irange(1, 3, -1)), [])


class RepresentationTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(repr(irange(10)), 'irange(0, 10)')
        self.assertEqual(repr(irange(2, 9)), 'irange(2, 9)')
        self.assertEqual(repr(irange(1, 5, 2)), 'irange(1, 5, 2)')
        self.assertEqual(repr(irange(5, 1, -2)), 'irange(5, 1, -2)')


class TrueBoolTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(bool(irange(5)))
        self.assertTrue(bool(irange(0, 4)))
        self.assertTrue(bool(irange(0, 6, 2)))
        self.assertTrue(bool(irange(4, 0, -1)))


class FalseBoolTestCase(unittest.TestCase):
    def test(self):
        self.assertFalse(bool(irange(5, 5)))
        self.assertFalse(bool(irange(6, 2)))
        self.assertFalse(bool(irange(1, 3, -1)))

def main():
    unittest.main()


if __name__ == "__main__":
    main()
