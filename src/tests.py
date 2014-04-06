import doctest
import ghdiff
import io
import os
import os.path
import sys
import tempfile
import unittest


class GhDiffTest(unittest.TestCase):

    def write_file(self, text):
        fd, path = tempfile.mkstemp()
        self._tempfiles.append(path)
        with os.fdopen(fd, "w") as f:
            f.write(text)
        return path

    def setUp(self):
        self._tempfiles = []
        self._stdout = sys.stdout

    def tearDown(self):
        for path in self._tempfiles:
            os.remove(path)
        del self._tempfiles[:]

    def test_script(self):
        """Simple exercise of the commandline mode"""
        f1 = self.write_file("foobar")
        f2 = self.write_file("foobarbaz")
        out = io.BytesIO()
        ghdiff.main([f1, f2], stdout=out)
        output = out.getvalue()
        self.assertTrue(b"-foobar" in output)
        self.assertTrue(b'+foobar<span class="highlight">baz</span>' in output)

    def test_no_css_option(self):
        """Simple test for --no-css option"""
        f1 = self.write_file("foobar")
        f2 = self.write_file("foobarbaz")
        out = io.BytesIO()
        ghdiff.main([f1, f2, "--no-css"], stdout=out)
        output = out.getvalue()
        self.assertFalse(b"<style" in output)


def test_suite():
    suite = unittest.makeSuite(GhDiffTest)
    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    suite.addTest(doctest.DocFileSuite("../README.rst", optionflags=flags))
    return suite
