import unittest
import decorator


class DecoratorTest(unittest.TestCase):
    def test_cache(self):
        query_one = decorator.sub(2, 1)
        query_two = decorator.sub(2, 1)

        self.assertTrue(query_one[0] == 0 and query_two[0] == 1)

    def test_function(self):
        query = decorator.sub(-5, 7)
        self.assertEqual(query[1], -12)


if __name__ == '__main__':
    unittest.main()
