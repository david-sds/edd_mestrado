#registrosregistrosregistrosregistros
import random

#matricula; salario; codigo setor

tamanho = 2

dicionario = {f'matricula {i}': random.randint(100000000, 999999999)
              for i in range(1, tamanho + 1)}

print(dicionario)
