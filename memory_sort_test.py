import unittest
import memorySort


class SortTest(unittest.TestCase):
    def test_sort_method(self):
        memorySort.sort("input.txt", "output.txt")
        self.assertTrue(memorySort.is_sorted("output.txt"))

    def test_wrong_files(self):
        self.assertRaises(FileNotFoundError, memorySort.sort, "isdjfisd.txt", "fjdisjf.txt")

    def test_is_sorted_method(self):
        self.assertFalse(memorySort.is_sorted("bad_output.txt"))


if __name__ == '__main__':
    unittest.main()
