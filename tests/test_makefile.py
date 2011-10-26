import unittest
from os.path import join, abspath, dirname, exists
from os import remove

try:
    from aps.makefile import *
except ImportError:
    import sys
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'aps')
    sys.path.append(srcpath)
    from makefile import *

class test_base(unittest.TestCase):

    def test_get_values(self):
        makefile = Makefile("uno", "arduino-sdk")
        self.assertEqual(makefile.speed,'115200') 

    def test_generate_makefile(self):
        makefile = Makefile("uno", "arduino-sdk")
        self.assertEqual(makefile.save("."), True)
        self.assertEqual(exists("Makefile"), True)
        try:
            remove("Makefile")
        except:
            pass

unittest.main()

