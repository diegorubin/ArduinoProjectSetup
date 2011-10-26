# -*- coding: utf-8 -*-

class Project():
    def __init__(self, destiny, arduino_sdk_path):
        self.__arduino_sdk_path__ = arduino_sdk_path
        self.__destiny__ = destiny

    def generate_makefile(self,path_to_makefile):
        original_content = open(entrada,"r").read()
    
        #TODO: Aqui ficará o código para tratar
        #      a manipulação do conteudo no antigo makefile
        #      e a criação no novo.
        new_content = original_content

        fileout = open(saida,"w")
        fileout.write(new_content)
