#registrosregistrosregistrosregistros
import random

#matricula; salario; codigo setor

tamanho = 100
lista_dict = []

for _ in range(1, tamanho+1):
    registros = {
        'matricula': random.randint(100000000, 999999999),
        'salario': random.randint(1000, 9999),
        'código': random.randint(100, 999)
    }
    lista_dict.append(registros)

for registros in lista_dict:
    print(registros)
    