
testipynb
=========

.. image:: https://img.shields.io/pypi/v/testipynb.svg
    :target: https://pypi.python.org/pypi/testipynb
    :alt: Latest PyPI version

.. image:: https://readthedocs.org/projects/testipynb/badge/?version=latest
    :target: http://testipynb.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/simpeg-research/heagy_2018_AEM.svg?branch=master
    :target: https://travis-ci.org/simpeg-research/heagy_2018_AEM
    :alt: Travis CI build status

.. image:: https://img.shields.io/github/license/lheagy/testipynb.svg
    :target: https://github.com/lheagy/testipynb/blob/master/LICENSE
    :alt: MIT license

Unit-testing for a collection of jupyter notebooks. :code:`testipynb` relies on `nbconvert <https://nbconvert.readthedocs.io>`_ to run the notebooks and catches errors so that they are output (with syntax highlighting!) when unit-tests are run.

why?
----

- If you want to share your notebooks and be confident that they _should_ work on someone else's machine
- If you are using notebooks to generate figures in a publication and want to ensure they are reproducible (powerful when connected with `cron jobs on travis-ci <https://docs.travis-ci.com/user/cron-jobs/>`_)

.. image:: https://raw.githubusercontent.com/lheagy/testipynb/master/docs/images/testing_syntax_highlighting.png
    :width: 80%
    :align: center

installation
------------

.. code::

    pip install testipynb

usage
-----

.. code:: python

    import testipynb
    import unittest

    NBDIR = '../notebooks'

    class TestNotebooks(unittest.TestCase):

        def test_notebooks(self):
            Test = testipynb.TestNotebooks(directory=NBDIR)
            self.assertTrue(Test.run_tests())

    if __name__ == "__main__":
        unittest.main()

