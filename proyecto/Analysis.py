class Analysis(object):
    def __init__(self, cases, results):
        self.cases = cases
        self.results = results

    def show(self):
        for result in self.results:
            estado = ''
            if result['status'] == False:
                estado = 'Fallido'
            else:
                estado = 'Exitoso'
            print(f'caso {result["case_id"]}: {estado}')