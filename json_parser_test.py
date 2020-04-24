import unittest
import json_parser
import json


class TestJsonParser(unittest.TestCase):
    def test_parser(self):
        key = 5
        z = {key: "z", 4: "zz", 3: [1, 2, 3]}
        a = {None: (1, 2, 3), "adsoko": z}
        b = [1, "4", a]

        self.assertEqual(json_parser.to_json(b), json.dumps(b))

    def test_exception(self):
        dictionary = {(1, 2): 2}
        self.assertRaises(TypeError, json_parser.to_json, dictionary)


if __name__ == '__main__':
    unittest.main()
