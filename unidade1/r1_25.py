'''
Solução 1

import string
def stripString(str):
    return str.translate(str.maketrans('','',string.punctuation))

print(stripString('Vamos tentar, Miguel!'))

'''


'''
Solução 2

'''
def stripString(str):
    # 'r’,.;:?!−_()[]∖’∖”‘/<>{}#=’'
    ponctuation=[',','.','!','?','/',"\\",'#','{','}','"',"'",'+','-','=','(',')','_',';',':','[',']','<','>']
    strip_string=str
    for p in ponctuation:
        strip_string=strip_string.replace(p,'')
    return strip_string

print(stripString('[/\Vamos tentar, Miguel!!!##.,'))