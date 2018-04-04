import testipynb
import os
import unittest

class TestClassAttributes(unittest.TestCase):

    def test_class_attributes(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-1] +
            ['notebooks', 'passing_notebooks']
        )
        Test = testipynb.TestNotebooks(directory=directory)

        nbnames = ['HelloWorld', 'notebook_that_loads_things']
        self.assertTrue(
            sorted(Test._nbnames) ==
            sorted(nbnames)
        )

        self.assertTrue(
            sorted(Test._nbpaths) ==
            sorted([
                directory + os.path.sep + "{}.ipynb".format(nb)
                for nb in nbnames
            ])
        )

class TestMyNotebooks(unittest.TestCase):

    def test_passing_notebooks(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-1] +
            ['notebooks', 'passing_notebooks']
        )
        Test = testipynb.TestNotebooks(directory=directory)
        self.assertTrue(Test.run_tests())

    def test_skipping_notebooks(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-1] +
            ['notebooks']
        )
        Test = testipynb.TestNotebooks(
            directory=directory,
            ignore=["failing_notebook", "failing_notebook2"]
        )
        self.assertTrue(Test.run_tests())

    @unittest.expectedFailure
    def test_simple_fail(self):
        directory = os.path.sep.join(
            os.path.abspath(__file__).split(os.path.sep)[:-1] +
            ['notebooks', 'failing_notebooks']
        )

        Test = testipynb.TestNotebooks(directory=directory)
        self.assertTrue(Test.run_tests())


if __name__ == "__main__":
    unittest.main()
