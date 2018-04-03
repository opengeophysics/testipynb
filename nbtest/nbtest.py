import unittest
import sys
import os
import pprint
import nbformat
from nbconvert.preprocessors import (
    ClearOutputPreprocessor, ExecutePreprocessor
)
from nbconvert.preprocessors.execute import CellExecutionError
import properties


__all__ = ['TestNotebooks']


def get_test(nbname, nbpath):

    # use nbconvert to execute the notebook
    def test_func(self):
        passing = True
        print(
            "\n--------------------- Testing {0}.ipynb ---------------------".format(nbname)
        )

        if nbname in self.py2_ignore and sys.version_info[0] == 2:
            print(" Skipping {}".format(nbname))
            return

        ep = ClearOutputPreprocessor()

        with open(nbpath) as f:
            nb = nbformat.read(f, as_version=4)

            ep.preprocess(nb, {})

            ex = ExecutePreprocessor(
                timeout=600,
                kernel_name='python{}'.format(sys.version_info[0]),
                allow_errors=True
            )

            out = ex.preprocess(nb, {})

            for cell in out[0]['cells']:
                if 'outputs' in cell.keys():
                    for output in cell['outputs']:
                        if output['output_type'] == 'error':
                            passing = False

                            err_msg = []
                            for o in output['traceback']:
                                err_msg += ["{}".format(o)]
                            err_msg = "\n".join(err_msg)

                            msg = """
\n ... {} FAILED \n
{} in cell [{}] \n-----------\n{}\n-----------\n
                            """.format(
                                nbname, output['ename'],
                                cell['execution_count'], cell['source'],
                            )

                            traceback = """
----------------- >> begin Traceback << ----------------- \n
{}\n
\n----------------- >> end Traceback << -----------------\n
                            """.format(err_msg)

                            print(u"{}".format(msg + traceback))

                            assert passing, msg #+ traceback

            print("   ... {0} Passed \n".format(nbname))

    return test_func


class TestNotebooks(properties.HasProperties, unittest.TestCase):

    name = properties.String(
        "test name",
        default = "NbTestCase"
    )

    directory = properties.String(
        "directory where the notebooks are stored",
        required=True,
        default='.'
    )

    py2_ignore = properties.List(
        "list of notebook names to ignore if testing on python 2",
        properties.String("file to ignore"),
        default=[]
    )

    nbpaths = properties.List(
        "paths to all of the notebooks",
        properties.String("path to notebook")
    )

    nbnames = properties.List(
        "names of all of the notebooks",
        properties.String("name of notebook")
    )

    @properties.validator('directory')
    def _use_abspath(self, change):
        change['value'] = os.path.abspath(change['value'])

    def __init__(self, **kwargs):
        super(TestNotebooks, self).__init__(**kwargs)
        nbpaths = []  # list of notebooks, with file paths
        nbnames = []  # list of notebook names (for making the tests)

        # walk the test directory and find all notebooks
        for dirname, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                if (
                    filename.endswith(".ipynb") and not
                    filename.endswith("-checkpoint.ipynb")
                ):
                    # get abspath of notebook
                    nbpaths.append(
                        dirname + os.path.sep + filename
                    )
                    # strip off the file extension
                    nbnames.append("".join(filename[:-6]))
        self.nbpaths = nbpaths
        self.nbnames = nbnames

    def get_tests(self):
        tests = dict()

        # build test for each notebook
        for nb, nbpath in zip(self.nbnames, self.nbpaths):
            tests["test_"+nb] = get_test(nb, nbpath)

        # create class to unit test notebooks
        NbTestCase = type("{}".format(self.name), (unittest.TestCase,), tests)
        NbTestCase.py2_ignore = self.py2_ignore
        return unittest.TestSuite(map(NbTestCase, tests.keys()))

    def run_tests(self, verbose=True):
        tests = self.get_tests()
        result = unittest.TestResult()
        testRunner = unittest.TextTestRunner()
        result = testRunner.run(tests)
        return result.wasSuccessful()


