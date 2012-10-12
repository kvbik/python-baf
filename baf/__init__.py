"""\
an example packaging layout

see https://github.com/kvbik/python-baf for more
"""

from baf import version

VERSION = version.VERSION
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

