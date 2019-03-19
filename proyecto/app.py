from Medias import Media

if __name__ == "__main__":
    medias = Media();
    vals = [5, 3, 12]

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