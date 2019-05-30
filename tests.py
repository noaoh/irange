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
        z = irange(1, 10, 2)
        x = [*z]
        self.assertEqual(repr(z), 'irange(1, 10, 2)')


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


class LengthTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(len(irange(5)), len(list(irange(5))))
        self.assertEqual(len(irange(2, 6)), len(list(irange(2, 6))))
        self.assertEqual(len(irange(-2, 5)), len(list(irange(-2, 5))))
        self.assertEqual(len(irange(2, 10, 2)), len(list(irange(2, 10, 2))))
        self.assertEqual(len(irange(5, 0, -2)), len(list(irange(5, 0, -2))))
        self.assertEqual(len(irange(-2, -6, -3)),
                         len(list(irange(-2, -6, -3))))
        self.assertEqual(len(irange(0, 7, 2)), len(list(irange(0, 7, 2))))
        self.assertEqual(len(irange(-2, -10, -2)),
                         len(list(irange(-2, -10, -2))))


class ContainsTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(5 in irange(5))
        self.assertTrue(0 in irange(5))
        self.assertTrue(8 in irange(2, 10))
        self.assertTrue(9 in irange(1, 10, 4))
        self.assertTrue(-1 in irange(-5, 0, 2))
        self.assertTrue(-4 in irange(-6, -2, 2))
        self.assertFalse(0 in irange(-5, 0, 2))
        self.assertFalse(10 in irange(1, 10, 4))
        self.assertFalse(5 in irange(5, 5))
        self.assertFalse(-6 in irange(-2, -6, -3))
        self.assertFalse(11 in irange(1, 10))
        self.assertFalse(0 in irange(1, 10))


class GetItem(unittest.TestCase):
    def test(self):
        with self.assertRaises(IndexError):
            irange(1, 10)[11]

        with self.assertRaises(IndexError):
            irange(1, 10)[-12]

        self.assertEqual(irange(10)[0], list(irange(10))[0])
        self.assertEqual(irange(10)[10], list(irange(10))[10])
        self.assertEqual(irange(10)[-2], list(irange(10))[-2])
        self.assertEqual(irange(2, 6)[3], list(irange(2, 6))[3])
        self.assertEqual(irange(-2, 10, 2)[3], list(irange(-2, 10, 2))[3])
        self.assertEqual(irange(5, 0, -2)[1], list(irange(5, 0, -2))[1])
        self.assertEqual(irange(5, 0, -2)[-2], list(irange(5, 0, -2))[-2])
        self.assertEqual(irange(0, 7, 2)[-1], list(irange(0, 7, 2))[-1])
        self.assertEqual(irange(-2, -10, -2)[3], list(irange(-2, -10, -2))[3])
        self.assertEqual(irange(-2, -8, -2)[-2], list(irange(-2, -8, -2))[-2])


class ReversedTestCase(unittest.TestCase):
    def test(self):
        def reverse_irange(x): return list(reversed(x))
        def reverse_list(x): return list(reversed(list(x)))
        self.assertEqual(reverse_irange(irange(10)), reverse_list(irange(10)))
        self.assertEqual(reverse_irange(irange(2, 6)),
                         reverse_list(irange(2, 6)))
        self.assertEqual(reverse_irange(irange(2, 8, 2)),
                         reverse_list(irange(2, 8, 2)))
        self.assertEqual(reverse_irange(irange(-2, 10, 2)),
                         reverse_list(irange(-2, 10, 2)))
        self.assertEqual(reverse_irange(irange(5, 0, -2)),
                         reverse_list(irange(5, 0, -2)))
        self.assertEqual(reverse_irange(irange(0, 7, 2)),
                         reverse_list(irange(0, 7, 2)))
        self.assertEqual(reverse_irange(irange(2, -10, -2)),
                         reverse_list(irange(2, -10, -2)))
        self.assertEqual(reverse_irange(irange(-2, -8, -2)),
                         reverse_list(irange(-2, -8, -2)))


class IndexTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            irange(1, 10).index(11)

        with self.assertRaises(ValueError):
            irange(1, 10).index(0)

        self.assertEqual(irange(10).index(10), list(irange(10)).index(10))
        self.assertEqual(irange(2, 6).index(3), list(irange(2, 6)).index(3))
        self.assertEqual(irange(2, 8, 2).index(
            6), list(irange(2, 8, 2)).index(6))
        self.assertEqual(irange(-2, 10, 2).index(0),
                         list(irange(-2, 10, 2)).index(0))
        self.assertEqual(irange(5, 0, -2).index(5),
                         list(irange(5, 0, -2)).index(5))
        self.assertEqual(irange(0, 7, 2).index(
            6), list(irange(0, 7, 2)).index(6))
        self.assertEqual(irange(2, -10, -2).index(0),
                         list(irange(2, -10, -2)).index(0))
        self.assertEqual(irange(-2, -8, -2).index(-4),
                         list(irange(-2, -8, -2)).index(-4))


class CountTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(irange(5).count(5), 1)
        self.assertEqual(irange(5).count(0), 1)
        self.assertEqual(irange(2, 10).count(8), 1)
        self.assertEqual(irange(1, 10, 4).count(9), 1)
        self.assertEqual(irange(-5, 0, 2).count(-1), 1)
        self.assertEqual(irange(-6, -2, 2).count(-4), 1)
        self.assertEqual(irange(-5, 0, 2).count(0), 0)
        self.assertEqual(irange(1, 10, 4).count(10), 0)
        self.assertEqual(irange(5, 5).count(5), 0)
        self.assertEqual(irange(-2, -6, -3).count(6), 0)
        self.assertEqual(irange(1, 10).count(11), 0)
        self.assertEqual(irange(1, 10).count(0), 0)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
