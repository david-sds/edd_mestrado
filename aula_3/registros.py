#registrosregistrosregistrosregistros
import random

#matricula; salario; codigo setor
count = 1
tamanho = 10
lista_dict = []

for count in range(1, tamanho+1):
    registros = {
        f'matricula {count}': random.randint(100000000, 999999999)
    }
    lista_dict.append(registros)

for registros in lista_dict:
    print(registros)
    





