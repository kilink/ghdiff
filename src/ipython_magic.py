from IPython.core.magic import Magics, line_magic, magics_class
from IPython.core import magic_arguments
from IPython.core.error import UsageError
from IPython.core.display import HTML

import ghdiff


@magics_class
class GHDiffMagics(Magics):

    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
            "var1",
            help="first variable"
        )
    @magic_arguments.argument(
            "var2",
            help="second variable"
        )
    @line_magic
    def ghdiff(self, line):
        """
        Generate Github-style HTML for unified diffs
        """
        args = magic_arguments.parse_argstring(self.ghdiff, line)
        try:
            a = self.shell.user_ns[args.var1]
        except KeyError:
            raise UsageError("Unknown variable %s" % args.var1)
        try:
            b = self.shell.user_ns[args.var2]
        except KeyError:
            raise UsageError("Unknown variable %s" % args.var2)
        return HTML(ghdiff.diff(a, b))

