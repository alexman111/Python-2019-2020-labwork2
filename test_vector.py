import unittest
from vector import Vector


class VectorTest(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Vector([1, 0, 4, 8]) + Vector([0, -1, 9, 90]), Vector([1, -1, 13, 98]))

    def test_substruction(self):
        self.assertEqual(Vector([1, 2, 3, 4]) - Vector([5, 6, 7, 8]), Vector([-4, -4, -4, -4]))

    def test_multiplication(self):
        self.assertEqual(Vector([5, 4, 3, 2]) * Vector([1, 2, 0.5, 1]), 16.5)

    def test_equality(self):
        v1 = Vector([1, 2, 3]) + Vector([2, 0, 1])
        v2 = Vector([3, 2, 4])
        self.assertTrue(v1 == v2)

    def test_len(self):
        self.assertTrue(len(Vector([1, 2])) == 2)

    def test_index(self):
        self.assertTrue(Vector([2, 4, 6])[2] == 6)

    def test_to_str(self):
        self.assertTrue(str(Vector([1, 2, 3])) == "[1, 2, 3]")

    def test_type(self):
        self.assertRaises(TypeError, Vector.__add__, Vector([1, 2]), [1])

    def test_index_overflow(self):
        self.assertRaises(IndexError, Vector.__getitem__, Vector([1, 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()