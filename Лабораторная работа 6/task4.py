import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        table = []
        data = [line.rstrip().split(',') for line in f.readlines()]
        table.append(data)
        headers = table[0]
        table = table[1:]
        dict_ = []
        for i in table:
            dict_.append(dict(zip(headers, i)))
        return dict_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))