

def listInputs():
    a = 0
    b = 0
    c = 0

    try:
        a = int(input('Digite o valor para a: '))
        b = int(input('Digite o valor para b: '))
        c = int(input('Digite o valor para c: '))
        return [a, b, c]

    except Exception as err:
        return []


def showOptions(data):
    if len(data)>0:
        a,b,c=data
        result = []
        if a and b and c:
            if a == b+c:
                result.append('Soma')
            if c == a + b:
                result.append('Soma')
            if a == b-c:
                result.append('Subtração')
            if c == a-b:
                result.append('Subtração')
            if a == b*c:
                result.append('Multiplicação')
            if c == a*b:
                result.append('Multiplicação')
            if a == b/c:
                result.append('Divisão')
            if c == a/b:
                result.append('Divisão')
        return result

    return 'Não foi possível identicar a operação'
    


def main():
    inputsData = listInputs()
    opt=showOptions(inputsData)
    print(opt)


main()
