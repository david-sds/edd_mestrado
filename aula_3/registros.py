#registrosregistrosregistrosregistros
import random

#matricula; salario; codigo setor

tamanho = 2
dicionario_2 = {'brasil': 'sp'}

dicionario = {f'matricula {i}': random.randint(100000000, 999999999)
              for i in range(1, tamanho + 1)}

print(dicionario)
print(dicionario_2)
