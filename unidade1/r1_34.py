from random import randrange

def generateSpam(n):
    result=[]
    for _ in range(0,n):
        text = list('Eu nunca mais vou enviar spam para meus amigos novamente.')
        isPrintError = randrange(0,2)
        if isPrintError:
            while True:
                error_position = randrange(0, len(text))
                if text[error_position] != ' ':
                    break
            
            text[error_position] = chr(randrange(64,122))
        result.append(''.join(text))
    return result

x=generateSpam(100)
for i in range(len(x)):
    print(f'{i+1} - '+x[i])
