def get_count_char(str_):
    main_dict = {}
    str_ = str_.lower()
    for letter_ in str_:
        if letter_.isalpha():
            if letter_ in main_dict:
                main_dict[letter_] += 1
            else:
                main_dict[letter_] = 1
    return main_dict


def percent_(new_dict):
    sum_ = sum(new_dict.values())
    for number_ in new_dict:
        new_dict[number_] = round(new_dict[number_]/sum_*100, 2)
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_dict = get_count_char(main_str)

print(get_count_char(main_str))
print(percent_(main_dict))
