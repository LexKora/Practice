# попытка номер 3
empty = '-'
FIELD = {}
for i in range(1,4):
    for j in range(1,4):
        FIELD [int(str(i)+str(j))] = empty
def graphic_field(kvarg):
    if kvarg == None :
        kvarg = {}
    print(f'   1  2  3')
    print(f' 1 {FIELD.get(11)}  {FIELD.get(12)}  {FIELD.get(13)}')
    print(f' 2 {FIELD.get(21)}  {FIELD.get(22)}  {FIELD.get(23)}')
    print(f' 3 {FIELD.get(31)}  {FIELD.get(32)}  {FIELD.get(33)}')
graphic_field(FIELD)