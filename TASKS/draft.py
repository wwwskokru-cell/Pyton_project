print('hi')

'''
Задача: нужно вывести победные комбинации в покере по цифрам 1-13
'''
from collections import Counter

def get_user_input ():
    is_input_valid = True
    while is_input_valid:
        entering_numbers = input("Введите 5 чисел через запятую от 1 до 13: ").lower().strip()
        entering_numbers_list = entering_numbers.split(",")
        if len(entering_numbers_list) != 5:
            print("Введите 5 целых чисел")
            continue

        entering_numbers_int = []
        try:
            for i in entering_numbers_list:
                i = int(i)
                entering_numbers_int.append(i)
        except ValueError:
            print("Вводите пожалучта только целые числа")
            continue
               
        index = 0
        for num in entering_numbers_int:
            if 0 < num < 14:
                index += 1
                if index == 5:
                    is_input_valid = False
            else:
                print("Вводите только числа от 1 до 13")
                continue
    return entering_numbers_int 

def counting_pairs_set_card (entering_numbers_int ):
    answer = {
        "Пары" : 0,
        "Сет" : 0,
        "Карэ" : 0
    }
    num_dict = Counter(entering_numbers_int)

    for i in num_dict:
        if num_dict[i] == 2:
            answer["Пары"] += 1
        elif num_dict[i] == 3:
            answer["Сет"] += 1
        elif num_dict[i] == 4:
            answer["Каре"] += 1
    return answer

print (counting_pairs_set_card(get_user_input ()))
 