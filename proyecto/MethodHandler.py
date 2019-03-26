class Handler(object):
    '''Manejador de metodos por modulos'''
    def __init__(self, cases, module, the_class):
        self.cases = cases
        self.results = []
        try:
            self._class = getattr(__import__(module), the_class)
            self.__run_cases()
        except:
            print('No se encontró el modulo')
    
    def get_results(self):
        return self.results

    def __run_cases(self):
        instance = self._class()
        expected = None
        generated = None
        error_type = None
        for case in self.cases:
            try:
                attr = getattr(instance, case['func'])
                generated = attr(case['param'])
            except Exception as e:
                error_type = e.__str__()
            self.results.append(
                self.__build_results(case, generated, error_type)
            )
    
    def __build_results(self, case, generated, error_type):
        return {
            'case_id': case['id'],
            'generated': generated,
            'expected': case['result'],
            'error': error_type,
        }