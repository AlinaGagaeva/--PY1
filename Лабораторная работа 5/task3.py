from random import randint

def get_unique_list_numbers() -> list[int]:
    min_ = -10
    max_ = 10
    range_ = 15
    list_random = []
    while len(list_random) < range_:
        i = randint(min_, max_)
        if i not in list_random:
            list_random.append(i)
    return list_random

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))