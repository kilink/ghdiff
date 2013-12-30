import doctest


def test_suite():
    return doctest.DocFileSuite(
            "../README.rst", optionflags=(doctest.ELLIPSIS |
            doctest.NORMALIZE_WHITESPACE))
