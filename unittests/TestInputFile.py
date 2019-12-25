import os, sys
from unittest import TestCase

sys.path.append("/home/jujubits/MyRepos/Kashmir/Application")
from InputFile import InputFile

class TestInputFile(TestCase):
    
    def setUp(self):
        self.test_dir = "Grandparent/Parent/Teen/Accident/test.file.csv"

    def test_get_file_location(self):
        expected = "Grandparent/Parent/Teen/Accident"
        result = InputFile(self.test_dir)._get_file_location()
        self.assertEqual(result, expected)

    def test_get_file_basename(self):
        expected = "test.file.csv"
        result = InputFile(self.test_dir)._get_file_basename()
        self.assertEqual(result, expected)

    def test_parse_file_name(self):
        expected = ["test","file","csv"]
        result = InputFile(self.test_dir)._parse_file_name()
        self.assertEqual(result, expected)

    def test_get_file_extension(self):
        expected = "csv"
        result = InputFile(self.test_dir)._get_file_extension()
        self.assertEqual(result, expected)

    def test_get_file_rootname(self):
        expected = "test.file"
        result = InputFile(self.test_dir)._get_file_rootname()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()