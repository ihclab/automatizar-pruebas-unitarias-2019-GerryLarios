import sys
from Medias import Media
from Reader import ReaderCases

def calculate_media():
    medias = Media();
    print('Media aritemetica')
    print( medias.aritmetica([2,4,8]) )
    print( medias.aritmetica([1, 5]) )
    print( medias.aritmetica([1,2,4,8,16,32]) )
    print('Media geometrica')
    print( medias.geometrica([1,2,4,8,16,32]) )
    print( medias.geometrica([0]) )
    print( medias.geometrica([2,4,8]) )
    print('Media armonica')
    print( medias.armonica([2,4,8]) )
    print( medias.armonica([2,3,6]) )

def check_args():
    print(f'The name of the script: {sys.argv[0]}')
    print(f'The number of arguments (with the name of the script): {len(sys.argv)}')
    print(f'The the arguments: {sys.argv}')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('Necesitas agregar un argumento')
    else:
        reader = ReaderCases(sys.argv[1])
        for case in reader.get_cases():
            print(case)