import sys
from Reader import ReaderCases
from MethodHandler import Handler
from Analysis import Analysis

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception('Necesitas agregar los argumentos')
    else:
        reader = ReaderCases(sys.argv[1])
        try:
            handler = Handler(reader.get_cases(), sys.argv[2], sys.argv[3])
            analisys = Analysis(reader.get_cases(), handler.get_results())
            analisys.show()
            analisys.buid_report()
        except :
            print('Error al procesar los casos de prueba.')