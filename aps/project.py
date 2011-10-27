# -*- coding: utf-8 -*-

from os import mkdir
from os.path import join, abspath, exists, dirname
from shutil import copyfile

from aps.makefile import Makefile

import re

class Project():
    def __init__(self, destiny, arduino_sdk_path):
        self.__arduino_sdk_path__ = arduino_sdk_path
        self.__destiny__ = destiny
        
    def __copy_template_pde__(self):
        print self.__destiny__
        file_pde = re.search("(\/?\w+\/)*(\w+)", self.__destiny__).group(2)
        datapath = abspath(join(dirname(__file__),'data'))
        copyfile(datapath + "/template.pde", "%s/%s.pde"%(self.__destiny__, file_pde ))

    def generate(self):
        result = True

        #try:
        # Create directory project
        mkdir(self.__destiny__)

        self.__copy_template_pde__()

        #except:
        #    result = False

        return result
