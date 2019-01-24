
testipynb
=========

.. image:: https://img.shields.io/pypi/v/testipynb.svg
    :target: https://pypi.python.org/pypi/testipynb
    :alt: Latest PyPI version

.. image:: https://readthedocs.org/projects/nbtest/badge/?version=latest
    :target: http://nbtest.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/opengeophysics/testipynb.svg?branch=master
    :target: https://travis-ci.org/opengeophysics/testipynb
    :alt: Travis CI build status

.. image:: https://codecov.io/gh/opengeophysics/testipynb/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/opengeophysics/testipynb
    :alt: coverage

.. image:: https://img.shields.io/github/license/opengeophysics/testipynb.svg
    :target: https://github.com/opengeophysics/testipynb/blob/master/LICENSE
    :alt: MIT license

Unit-testing for a collection of jupyter notebooks. :code:`testipynb` relies on `nbconvert <https://nbconvert.readthedocs.io>`_ to run the notebooks and catches errors so that they are output (with syntax highlighting!) when unit-tests are run.

why?
----

- If you want to share your notebooks and be confident that they _should_ work on someone else's machine
- If you are using notebooks to generate figures in a publication and want to ensure they are reproducible (powerful when connected with `cron jobs on travis-ci <https://docs.travis-ci.com/user/cron-jobs/>`_)

.. image:: https://raw.githubusercontent.com/opengeophysics/testipynb/master/docs/images/testing_syntax_highlighting.png
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
    
    NBDIR = '../notebooks'
    
    Test = testipynb.TestNotebooks(directory=NBDIR)
    Test.assertTrue(Test.run_tests())

or in a unit-test file: 


.. code:: python

    import testipynb
    import unittest

    NBDIR = '../notebooks'

    Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2100)
    TestNotebooks = Test.get_tests()

    if __name__ == "__main__":
        unittest.main()


connections
-----------

:code:`testipynb` is used in:

- https://github.com/simpeg-research/heagy_2018_AEM

If you use :code:`testipynb` in one of your repositories and would like it listed, please `edit this file <https://github.com/lheagy/testipynb/edit/master/README.rst>`_ 
