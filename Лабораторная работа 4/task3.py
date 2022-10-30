def delete(list_, index=None):
    if index == None:
        index = -1
        return list_[:-1]
    elif index >= 0:
        list_a = list_[:index]
        list_b = list_[index+1:]
        return list_a + list_b
    else:
        list_c = list_[::-1]
        index = index * (-1) - 1
        list_d = list_c[:index]
        list_e = list_c[index+1:]
        list_f = list_d + list_e
        return list_f[::-1]
print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
