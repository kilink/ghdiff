import doctest

def test_suite():
    return doctest.DocFileSuite(
        "../README.txt", optionflags=(doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE))
