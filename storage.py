import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser(description='key+value')
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def not_empty_file():
    with open(storage_path, 'r') as f:
        if f.readlines() != []:
            return True
        else:
            return False

def search_exist(key):
    with open(storage_path, 'r') as f:
        if not_empty_file():
            load = json.load(f)
            if key in load.keys():
                return load.get(key)
            else:
                return None
        else:
            return 'empty'

def writing(key, value):
    if search_exist(key) == None:
        with open(storage_path, 'r') as f:
            load = json.load(f)
        new_dict = {key: [value]}
        load.update(new_dict)
        with open(storage_path, 'w') as f:
            json.dump(load, f)

    elif search_exist(key) == 'empty':
        with open(storage_path, 'w') as f:
            new_dict = {key: [value]}
            json.dump(new_dict, f)

    else:
        new_val = search_exist(key)
        new_val.append(value)
        new_dict = {key: new_val}
        with open(storage_path, 'r') as f:
            load = json.load(f)
        load.pop(key)
        load.update(new_dict)
        with open(storage_path, 'w') as f:
            json.dump(load, f)

if args.key != None:
    if args.val == None:
        if search_exist(args.key) == None or search_exist(args.key) == 'empty':
            print('None')
        else:
            print(', '.join(search_exist(args.key)))
    else:
        writing(args.key, args.val)