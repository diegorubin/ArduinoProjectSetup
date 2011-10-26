import re
from os.path import join, abspath, exists, dirname, exists

class Makefile():
    BOARDS_PATH = ("/hardware/arduino/boards.txt",
                   "/hardware/boards.txt")
    
    MAKEFILE_ATTRIBUTES = ["speed", "protocol", "mcu", "f_cpu"]

    def __init__(self, version, arduino_sdk_path):
        self.__version__ = version.lower()
        self.__arduino_sdk_path__ = arduino_sdk_path

        self.__get_values__()

    def __get_values__(self):

        regex = re.compile("%s\.\w+\.("%self.__version__ + "|".join(Makefile.MAKEFILE_ATTRIBUTES) + ")=(\w+)")

        board_path = None
        if exists(self.__arduino_sdk_path__ + Makefile.BOARDS_PATH[1]):
            board_path = self.__arduino_sdk_path__ + Makefile.BOARDS_PATH[1]
        else:
            board_path = self.__arduino_sdk_path__ + Makefile.BOARDS_PATH[0]


        board_raw = open(board_path, 'r')  
        for line in board_raw:
            m = regex.match(line)
            if m:
                setattr(self,m.group(1), m.group(2)) 

    # Public methods
    def save(self,path):
        result = True

        datapath = abspath(join(dirname(__file__), 'data'))
        raw_makefile = open(datapath + "/Makefile.arduino",'r').read()

        new_content = raw_makefile.replace("__VERSION__",self.__version__)
        for attr in Makefile.MAKEFILE_ATTRIBUTES:
            new_content = new_content.replace("__%s__"%attr.upper(),getattr(self,attr))
        
        try:
            new_makefile = open(path + "/Makefile", 'w')
            new_makefile.write(new_content)
            
        except:
            result = False

        return result
