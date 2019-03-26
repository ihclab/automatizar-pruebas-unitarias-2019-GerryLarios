import sys
import json
import datetime
import colorama
from colorama import Fore
class Analysis(object):
    def __init__(self, cases, results):
        self.cases = cases
        self.results = results

    def buid_report(self):

        report_name = datetime.datetime.now().strftime('%c').replace(' ', '-')

        with open(report_name + '.json', 'w') as fp:
            json.dump(self.results, fp)

    def show(self):
        for result in self.results:
            if result['status'] == False:
                print(f'{Fore.RED}caso {result["case_id"]}: Fallido')
            else:
                print(f'{Fore.GREEN}caso {result["case_id"]}: Exitoso')
            print(f'Tiempo de ejecución: {result["time_exe"]}\n')
