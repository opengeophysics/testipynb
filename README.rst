
nbtest
======

Unit-testing for a collection of jupyter notebooks. :code:`nbtest` relies on `nbconvert <https://nbconvert.readthedocs.io>`_ to run the notebooks and catches errors so that they are output (with syntax highlighting!) when unit-tests are run.

why?
----

- If you want to share your notebooks and be confident that they _should_ work on someone else's machine
- If you are using notebooks to generate figures in a publication and want to ensure they are reproducible (powerful when connected with `cron jobs on travis-ci <https://docs.travis-ci.com/user/cron-jobs/>`_)

installation
------------

.. code::

    pip install nbtest

usage
-----

.. code:: python

    import nbtest
    import os
    import sys
    import unittest

    NBDIR = '../notebooks'

    class TestFail(unittest.TestCase):

        def test_notebooks(self):
            Test = nbtest.TestNotebooks(directory=NBDIR)
            self.assertTrue(Test.run_tests())

    if __name__ == "__main__":
    unittest.main()

