.. image:: https://secure.travis-ci.org/kilink/ghdiff.png?branch=master
   :target: http://travis-ci.org/kilink/ghdiff

.. image:: https://coveralls.io/repos/kilink/ghdiff/badge.png
   :target: https://coveralls.io/r/kilink/ghdiff

ghdiff
======

Generate Github-style HTML for unified diffs.

Changes
-------


0.4 (2014-06-13)
~~~~~~~~~~~~~~~~

* Add iPython magic (mgaitan)

0.3 (2014-04-06)
~~~~~~~~~~~~~~~~

* Fix Python 3 issue when running as a command-line script.

0.2
~~~

* Detect character encoding when reading files (Nyoroon)
* PEP-8 clean up (laulaz)
* Fix display problem when text line is too long (laulaz)

0.1
~~~

* initial release.

diff
====

Generate a diff and output Github-style HTML for it.

.. code-block:: pycon

    >>> import ghdiff
    >>> from six import print_
    >>> print_(ghdiff.diff("a\nb", "b\nb"))
    <style type="text/css">
    ...
    </style>
    <div class="diff">
        <div class="control">@@&nbsp;-1,2&nbsp;+1,2&nbsp;@@
        </div>
        <div class="delete">-a</div>
        <div class="">&nbsp;b</div>
        <div class="insert">+b</div>
    </div>

The css option controls whether or not the output includes CSS.

.. code-block:: pycon

    >>> print_(ghdiff.diff("blah blah blah\nb", "blah zxqq blah\nb", css=False))
    <div class="diff">
        <div class="control">@@&nbsp;-1,2&nbsp;+1,2&nbsp;@@
        </div>
        <div class="delete">-blah&nbsp;<span class="highlight">blah</span>&nbsp;blah</div>
        <div class="insert">+blah&nbsp;<span class="highlight">zxqq</span>&nbsp;blah</div>
        <div class="">&nbsp;b</div>
    </div>

diff accepts lists of strings representing lines as well.

.. code-block:: pycon

    >>> print_(ghdiff.diff(["blah blah blah", "b"], ["blah zxqq blah", "b"]))
    <style type="text/css">
    ...
    </style>
    <div class="diff">
        <div class="control">@@&nbsp;-1,2&nbsp;+1,2&nbsp;@@
        </div>
        <div class="delete">-blah&nbsp;<span class="highlight">blah</span>&nbsp;blah</div>
        <div class="insert">+blah&nbsp;<span class="highlight">zxqq</span>&nbsp;blah</div>
        <div class="">&nbsp;b</div>
    </div>

IPython magic
=============

ghdiff also works as an IPython magic:

.. code-block:: python

    In[1]: %load_ext ghdiff

    In[2]: %ghdiff var1 var2

See a `notebook example <http://nbviewer.ipython.org/github/kilink/ghdiff/blob/master/demo.ipynb>`_


colorize
========

colorize takes an existing unified diff and outputs Github-style markup.

.. code-block:: python

    >>> print_(ghdiff.colorize("""\
    ... index 921100e..8b177e1 100755
    ... --- a/src/ghdiff.py
    ... +++ b/src/ghdiff.py
    ... @@ -10,20 +10,24 @@ def escape(text):
    ...  default_css = \"\"\"\
    ...  <style type="text/css">
    ...  %s
    ... -</style>\"\"\" % (open(os.path.join(os.path.dirname(__file__), "default.css")).read(),)
    ... +</style>
    ... +\"\"\" % (open(os.path.join(os.path.dirname(__file__), "default.css")).read(),)
    ... +"""))
    <style type="text/css">
    ...
    </style>
    <div class="diff">
    <div class="control">@@&nbsp;-10,20&nbsp;+10,24&nbsp;@@&nbsp;def&nbsp;escape(text):</div>
    <div class="">&nbsp;default_css&nbsp;=&nbsp;"""&nbsp;&lt;style&nbsp;type="text/css"&gt;</div>
    <div class="">&nbsp;%s</div>
    <div class="delete">-&lt;/style&gt;"""&nbsp;%&nbsp;(open(os.path.join(os.path.dirname(__file__),&nbsp;"default.css")).read(),)</div>
    <div class="insert">+&lt;/style&gt;</div>
    <div class="insert">+"""&nbsp;%&nbsp;(open(os.path.join(os.path.dirname(__file__),&nbsp;"default.css")).read(),)</div>
    <div class="insert">+</div>
    </div>
