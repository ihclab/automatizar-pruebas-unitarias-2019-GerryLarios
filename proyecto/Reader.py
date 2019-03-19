import sys
class ReaderCases(object):
    '''Lector de archivos de texto plano'''
    def __init__(self, filename):
        self.cases = []
        try:
            self.file = open(filename, mode = 'r')
            self.__read_file()
        except FileNotFoundError as e:
            print('[ERROR] no se ha podido abrir el archivo')
    
    def __read_file(self):
        self.file.seek(0, 0)
        for line in self.file.readlines():
            self.cases.append(self.__parsing(line))
    
    def __parsing(self, line):
        return line.replace('\n','').split(':')

    def get_cases(self):
        return self.cases