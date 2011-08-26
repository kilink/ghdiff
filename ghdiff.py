#!/usr/bin/python

import difflib
import xml.sax.saxutils

def escape(text):
    return xml.sax.saxutils.escape(text, {" ": "&nbsp;"})

default_css = """\
<style type="text/css">
    .diff {
        border: 1px solid #cccccc;
        background: none repeat scroll 0 0 #f8f8f8;
        font-family: 'Bitstream Vera Sans Mono','Courier',monospace;
        font-size: 12px;
        line-height: 1.4;
    }
    .diff div:hover {
        background-color:#ffc;
    }
    .diff .control {
        background-color: #eaf2f5;
        color: #999999;
    }
    .diff .insert {
        background-color: #ddffdd;
        color: #000000;
    }
    .diff .insert .highlight {
        background-color: #aaffaa;
        color: #000000;
    }
    .diff .delete {
        background-color: #ffdddd;
        color: #000000;
    }
    .diff .delete .highlight {
        background-color: #ffaaaa;
        color: #000000;
    }
</style>
"""

def diff(a, b, n=3, css=True):
    output = ['<div class="diff">']
    if css:
        output.insert(0, default_css)
    matcher = difflib.SequenceMatcher(a=a, b=b)
    for group in matcher.get_grouped_opcodes(n):
        i1, i2, j1, j2 = group[0][1], group[-1][2], group[0][3], group[-1][4]
        output.append(
            '<div class="control">@@ -%d,%d +%d,%d @@</div>' % (
                i1+1, i2-i1, j1+1, j2-j1))
        for tag, i1, i2, j1, j2 in group:
            if tag == "equal":
                for line in a[i1:i2]:
                    output.append("<div>%s</div>" % escape(line or " ",))
                continue
            if tag == "replace":
                alines = []
                blines = []
                for i, line in enumerate(a[i1:i2]):
                    aline, bline = _line_diff(line, b[j1:j2][i])
                    alines.append(aline)
                    blines.append(bline)
                for line in alines:
                    output.append('<div class="delete">-%s</div>'% (line,))
                for line in blines:
                    output.append('<div class="insert">+%s</div>'% (line,))
            if tag == "delete":
                for line in a[i1:i2]:
                    output.append(
                        '<div class="delete">-%s</div>'% (escape(line),))
            if tag == "insert":
                for line in b[j1:j2]:
                    output.append(
                        '<div class="insert">+%s</div>'% (escape(line),))
    output.append("</div>")
    return "\n".join(output)

def _line_diff(a, b):
    aline = []
    bline = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
        if tag == "equal":
            aline.append(escape(a[i1:i2]))
            bline.append(escape(b[j1:j2]))
            continue
        aline.append('<span class="highlight">%s</span>' % (escape(a[i1:i2]),))
        bline.append('<span class="highlight">%s</span>' % (escape(b[j1:j2]),))
    return "".join(aline), "".join(bline)


if __name__ == "__main__":
    import optparse
    import sys

    parser = optparse.OptionParser()
    parser.set_usage("%prog [options] file1 file2")
    parser.add_option("--no-css", action="store_false", dest="css",
                      help="Don't include CSS in output", default=True)

    options, args = parser.parse_args()

    if (len(args) != 2):
        parser.print_help()
        sys.exit(-1)

    a = open(sys.argv[1]).read().splitlines()
    b = open(sys.argv[2]).read().splitlines()
    print diff(a, b, css=options.css)
