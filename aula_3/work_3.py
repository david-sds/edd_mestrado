import numpy as np
import random

def hash_str(s):
    p = 31
    m = 10 ** 9 + 7
    hash_value = 0
    p_pow = 1
    
    for c in s:
        hash_value = (hash_value + (1 + ord(c) - ord('a')) * p_pow) % m
        p_pow = (p_pow * p) % m
        
    return hash_value

def module(val, k):
    key = hash_str(val) % k
    return key

def init_dict(dictionary, size):
    for _ in range(size):
        dictionary.append([])
        
def search_entry(dictionary, matricula, mod):
    key = module(matricula, mod)
    dict_list = dictionary[key]
    return next((x for x in dict_list if str(x['matricula']) == str(matricula)), None)

modules = [10] #[1000, 10000, 100000]
entries = [10] #[5000, 20000, 100000]

for mod in modules:
    hash_table = []
    init_dict(hash_table, mod)
    
    for entry_num in entries:
        for i in range(entry_num):
            entry = {
                'matricula': random.randint(100000000, 999999999),
                'salario': random.randint(1000, 9999),
                'codigo': random.randint(100, 999)
            }
            val = str(entry['matricula'])
            hash_key = module(val, mod)
            hash_table[hash_key].append(entry)

        for i in range(len(hash_table)):
            print(hash_table[i])

    is_exit = False
    while is_exit != True:
        user_input = input('Search matricula (0 to exit): ')
        if (user_input == '0'):
            is_exit = True
        print(search_entry(hash_table, user_input, mod))