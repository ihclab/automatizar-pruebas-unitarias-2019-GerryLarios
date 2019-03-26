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
        exc_type = None
        for case in self.cases:
            try:
                attr = getattr(instance, case['func'])
                print(case['result'])
                generated = attr(case['param'])
            except Exception as e:
                exc_type = e.__str__()
            self.results.append(
                self.__build_results(case, generated, exc_type)
            )
    
    def __build_results(self, case, generated, exc_type):

        status = False

        if case['result'] == 'Exception' and exc_type != None:
            status = True
        else:
            if case['result'] == generated:
                status = True

        return {
            'case_id': case['id'],
            'status': status,
            'generated': generated,
            'expected': case['result'],
            'exception': exc_type,
        }