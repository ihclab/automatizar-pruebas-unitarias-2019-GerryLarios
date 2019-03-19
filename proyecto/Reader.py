import sys
class Reader(object):
    '''Lector de archivos de texto plano'''
    def __init__(self, filename):
        try:
            self.file = open(filename, mode = 'r')
            self.__read_file()
        except FileNotFoundError as e:
            print('[ERROR] no se ha podido abrir el archivo')
    
    def __read_file(self):
        self.file.seek(0, 0)
        for line in self.file.readlines():
            print(line)