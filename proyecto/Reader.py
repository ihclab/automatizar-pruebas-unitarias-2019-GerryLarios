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
                'func': vec[1],
                'param': self.__convert_values(vec[2]),
                'result': self.__convert_result(vec[3])
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

    def __convert_result(self, result):
        try:
            return float(result)
        except:
            return result

    def get_cases(self):
        return self.cases