letter_nb_convertor = {'A':1, "B":2, "C":3, 'D':4, 'E':5,
                       "F":6, "G":7, "H":8, "I":9, "J":10,
                       "K":11, "L":12, "M":13, 'N':14, 'O':15,
                       "P":16, 'Q':17, 'R':18, 'S':19, 'T':20,
                       'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
nb_letter_converter = ['']
nb_letter_converter.extend(list(letter_nb_convertor.keys()))
def coordinate_type(c):
    if 'R' in c and 'C' in c and c.index('C') - c.index('R') > 0:
        return 'RC'
    else:
        return 'LN'
def LNtoRC(c):
    col = 0
    for i in c:
        if i in letter_nb_convertor:
            col +=26
            add = letter_nb_convertor[i]
            c=c.replace(i, '')
    col +=add
    return "R{}C{}".format(c, col)
def RCtoLN(c):
    new_col = ''
    c =c.replace('R', '')
    row, col = tuple(c.split('C'))
    new_col+=nb_letter_converter[int(col)//26]
    new_col+=nb_letter_converter[int(col)%26]
    return "{}{}".format(new_col, row)
n = int(input("Enter the number of coordinates"))
coordinates = []
for i in range(n):
    print("Enter the coordinates of the cell:", end='')
    c = input()
    coordinates.append(c)
for i in coordinates:
    if coordinate_type(i) == 'LN':
        print(LNtoRC(i))
    else:
        print(RCtoLN(i))