import nbtest
import os
import unittest


class TestMyNotebooks(unittest.TestCase):

    def test_passing_notebooks(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-2] +
            ['notebooks/passing_notebooks']
        )
        Test = nbtest.TestNotebooks(directory=directory)
        self.assertTrue(Test.run_tests())

class TestFail(unittest.TestCase):

    @unittest.expectedFailure
    def test_simple_fail(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-2] +
            ['notebooks/failing_notebooks']
        )

        Test = nbtest.TestNotebooks(directory=directory)
        self.assertTrue(Test.run_tests())


if __name__ == "__main__":
    unittest.main()
