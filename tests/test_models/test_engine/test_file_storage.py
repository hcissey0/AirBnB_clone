#!/usr/bin/python3
"""This is the file storage test file"""

from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """This is the file storage unittest case"""

    def test_is_instance(self):
        fs = FileStorage()

        self.assertTrue(isinstance(fs, FileStorage))

    def test_documentations(self):
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)
        self.assertTrue(len(FileStorage.delete.__doc__) > 1)
        self.assertTrue(len(FileStorage.update.__doc__) > 1)


if __name__ == '__main__':
    unittest.main()
