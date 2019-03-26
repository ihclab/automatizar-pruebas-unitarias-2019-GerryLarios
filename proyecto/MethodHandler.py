class Handler(object):
    '''Manejador de metodos por modulos'''
    def __init__(self, cases, module, the_class):
        self.cases = cases
        try:
            self._class = getattr(__import__(module), the_class)
            self.__check_methods()
        except:
            print('No se encontró el modulo')
    
    def __check_methods(self):
        for case in self.cases:
            try:
                func = getattr(self._class, case['func'])
            except:
                print('Metodo no encontrado')