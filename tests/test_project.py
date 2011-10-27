import unittest
from os.path import join, abspath, dirname, exists
from os import removedirs
from shutil import rmtree

try:
    from aps.project import *
except ImportError:
    import sys
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    srcpath = join(parentpath, 'aps')
    sys.path.append(srcpath)
    from project import *

class test_base(unittest.TestCase):

    def test_generate_directory_project(self):
        project = Project("exemplo", "arduino-sdk")
        self.assertEqual(project.generate(), True)
        self.assertEqual(exists("exemplo/exemplo.pde"), True)
        try:
            rmtree("exemplo")
        except:
            pass

unittest.main()

