import random

def my_choice(list):
    try:
        if len(list)>0:
            choiceIndex=random.randrange(0,len(list))
            return list[choiceIndex]
        else:
            print('Não foi informado o tamanho da list')
            raise ValueError('Lista vazia','Error no código')
    except ValueError as err:
        raise print(err.args)

mylist = ['Xenopus laevis','Homo sapiens','Felis catus']

print(my_choice(mylist))

# print(random.randrange(3, 9))