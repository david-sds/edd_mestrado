import random
import time
import math
import secrets


test_list = [
    {'matricula': 141262611, 'salario': 5607, 'codigo': 522}, 
    {'matricula': 414100591, 'salario': 5582, 'codigo': 159},
    {'matricula': 412040462, 'salario': 7723, 'codigo': 663},
    {'matricula': 173958745, 'salario': 1549, 'codigo': 366},
    {'matricula': 734104246, 'salario': 5767, 'codigo': 235}, 
    {'matricula': 959742316, 'salario': 7290, 'codigo': 273}, 
    {'matricula': 228044966, 'salario': 6271, 'codigo': 470},
    {'matricula': 321726248, 'salario': 7187, 'codigo': 305}, 
    {'matricula': 675370468, 'salario': 8271, 'codigo': 574}, 
    {'matricula': 342323178, 'salario': 9734, 'codigo': 257}
]

def module(val, k):
    key = int(val) % k
    return key

def init_dict(dictionary, size):
    for _ in range(size):
        dictionary.append([])
        
def search_entry(dictionary, matricula, mod):
    key = module(matricula, mod)
    dict_list = dictionary[key]
    return next((x for x in dict_list if str(x['matricula']) == str(matricula)), None)

def add_entry(dictionary, entry, **kwargs):
    collisions = kwargs.get('collisions', None)
    is_collisions = collisions != None
    val = entry['matricula']
    hash_key = module(val, mod)
    if is_collisions and len(hash_table[hash_key]) > 0:
        collisions[hash_key] += 1
    dictionary[hash_key].append(entry)

modules = [1000, 10000, 100000]
entries = [5000, 20000, 100000]


for mod in modules:
    hash_table = []
    init_dict(hash_table, mod)
    
    for entry_num in entries:
        collisions_list = [0] * mod
        for i in range(entry_num - len(test_list)):
            entry = {
                'matricula': random.randint(100000000, 999999999),
                'salario': random.randint(1000, 9999),
                'codigo': random.randint(100, 999)
            }
            add_entry(hash_table, entry, collisions=collisions_list)
        for entry in test_list:
            add_entry(hash_table, entry, collisions=collisions_list)
                
        time_sum = 0
        for entry in test_list:
            start_time = time.time() * 1000
            search_entry(hash_table, entry['matricula'], mod)
            end_time = time.time() * 1000
            time_sum += (end_time - start_time)
        
        print('MODULOS:', mod)
        print('ITENS', entry_num)
        print('colisoes:', sum(collisions_list))
        print(f'tempo medio de busca {time_sum / len(test_list)}ms')
        media = sum(collisions_list) / entry_num
        print('media', media)
        
        aux = []
        for i in collisions_list:
            if i == 0:
                continue
            aux.append(math.pow(media - i, 2))
        desvio_padrao = math.sqrt(sum(aux) / len(aux))
        print('desvio padrao', desvio_padrao)
        print('')
        
        
hash_tables = []
common_lists = []

for i in range(10):
    hash_table = []
    init_dict(hash_table, 100000)
    hash_tables.append(hash_table)
    
    common_lists.append([])
    
    for j in range(100000):
        entry = {
            'matricula': random.randint(100000000, 999999999),
            'salario': random.randint(1000, 9999),
            'codigo': random.randint(100, 999)
        }
        add_entry(hash_tables[i], entry)
        common_lists[i].append(entry)

sum_hash_table = 0
sum_common_list = 0    
for i in range(10):
    hash_table = hash_tables[i]
    common_list = common_lists[i]
    item = secrets.choice(common_list)
    print(f'searching {item['matricula']}...')
    
    start_time = time.time() * 1000
    search_entry(hash_table, item['matricula'], mod)
    end_time = time.time() * 1000
    sum_hash_table += (end_time - start_time)
    
    start_time = time.time() * 1000
    for i in common_list:
        if i['matricula'] == item['matricula']:
            break;
    search_entry(hash_table, item['matricula'], mod)
    end_time = time.time() * 1000
    sum_common_list += (end_time - start_time)
    
print(f'tempo medio busca hash_table: {sum_hash_table / 10}ms')
print(f'tempo medio busca list: {sum_common_list / 10}ms')