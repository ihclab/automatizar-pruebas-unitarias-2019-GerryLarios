import sys
from Reader import ReaderCases
from MethodHandler import Handler
from Analysis import Analysis

def check_args():
    print(f'The name of the script: {sys.argv[0]}')
    print(f'The number of arguments (with the name of the script): {len(sys.argv)}')
    print(f'The the arguments: {sys.argv}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception('Necesitas agregar los argumentos')
    else:
        reader = ReaderCases(sys.argv[1])
        try:
            handler = Handler(reader.get_cases(), sys.argv[2], sys.argv[3])
            analisys = Analysis(reader.get_cases(), handler.get_results())
            analisys.show()
        except :
            print('Error al procesar los casos de prueba.')