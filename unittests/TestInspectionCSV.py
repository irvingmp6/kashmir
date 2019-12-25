import os, sys
from unittest import TestCase

sys.path.append("/home/jujubits/MyRepos/Kashmir/Application")
from FileInspectionCSV import FileInspectionCSV

class TestFileInspectionCSV(TestCase):
    
    def setUp(self):
        self.test_dir = "Grandparent/Parent/Teen/Accident/test.file.csv"

    def test_extension_check(self):
        expected = True
        result = FileInspectionCSV(self.test_dir)._extension_check()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()