======
ghdiff
======

ghdiff generates Github-style HTML for unified diffs.

diff
====

Generate a diff and output Github-style HTML for it.

    >>> import ghdiff
    >>> from pprint import pprint
    >>> print ghdiff.diff("a", "b")
    <style type="text/css">
    ...
    </style>
    <div class="diff">
        <div class="control">@@&nbsp;-1,1&nbsp;+1,1&nbsp;@@
        </div>
        <div class="delete">-<span class="highlight">a</span></div>
        <div class="insert">+<span class="highlight">b</span></div>
    </div>

The css option controls whether or not the output includes CSS.

    >>> print ghdiff.diff("blah blah blah\nb", "blah zxqq blah\nb", css=False)
    <div class="diff">
        <div class="control">@@&nbsp;-1,2&nbsp;+1,2&nbsp;@@
        </div>
        <div class="delete">-blah&nbsp;<span class="highlight">blah</span>&nbsp;blah</div>
        <div class="insert">+blah&nbsp;<span class="highlight">zxqq</span>&nbsp;blah</div>
        <div class="">&nbsp;b</div>
    </div>

diff accepts lists of strings representing lines as well.

    >>> print ghdiff.diff(["blah blah blah", "b"], ["blah zxqq blah", "b"])
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

colorize
========

colorize takes an existing unified diff and outputs Github-style markup.

    >>> print ghdiff.colorize("""\
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
    ... +""")
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