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
            vec = self.__parsing(line)
            self.cases.append({
                'id': vec[0],
                'method': vec[1],
                'values': self.__convert_values(vec[2]),
                'result': vec[3]
            })
    
    def __parsing(self, line):
        return line.replace('\n','').split(':')

    def __convert_values(self, val):
        new_values = []
        for n in val.split(' '):
            try:
                new_values.append(float(n))
            except:
                new_values.append(None)
        return new_values

    def get_cases(self):
        return self.cases