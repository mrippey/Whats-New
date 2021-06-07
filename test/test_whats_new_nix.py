import unittest 
import pathlib 

class TestCaseBase(unittest.TestCase):
    def assertIsDir(self, path):
        if not pathlib.Path(path).resolve().is_dir():
            raise AssertionError(f'Dir does not exist {str(path)}')

class ActualTest(TestCaseBase):
    def test(self):
        path = pathlib.Path('/usr/bin/')
        self.assertIsDir(path)

if __name__ == "__main__":
    unittest.main()
