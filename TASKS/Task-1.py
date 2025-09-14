'''
Задача: нужно вывести победные комбинации в покере по цифрам 1-13
'''
from collections import Counter


def get_user_input ():
    #Ввалидация ввода пользователя

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

        if entering_numbers_int[0] == entering_numbers_int[1] == entering_numbers_int[2] == entering_numbers_int[3] == entering_numbers_int[4]:
            print("К сожалению в колоде только по 4 одинаковых карты, вы ввели 5, это недопустимо")
            continue
        
        if all(1<= num <= 13 for num in entering_numbers_int):
            return entering_numbers_int
        else:
            print("Вводите только числа от 1 до 13")
            continue

    return entering_numbers_int 


def counting_pairs_set_card (entering_numbers_int ):
    #Определение пара, сет, каре
    answer = {
        "Пары" : 0,
        "Сет" : 0,
        "Каре" : 0
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


def counting_street (entering_numbers_int):
    #Отпределение стрит
    number_int_sort = set(entering_numbers_int)
    number_int_sort = sorted(number_int_sort)
    checking_street = True
    if len(number_int_sort) == 5:
        for i in range(4):
            if number_int_sort[i+1]- number_int_sort[i] == 1:
                checking_street = True
            else:
                checking_street = False
                break
    else:
        checking_street = False               
    return checking_street


def answer_final (answer, checking_street, entering_numbers_int):
    #Подсчет результата

    answer_final_dict = {
        "Каре": 0,
        "Фул Хаус" : 0,
        "Стрит" : 0,
        "Сет" : 0,
        "2 Пары" : 0,
        "Пара" : 0
        }
    
    if answer["Каре"] == 1:
        answer_final_dict["Каре"] += 1 
    elif answer["Сет"] == 1 and answer["Пары"] == 1:
        answer_final_dict["Фул Хаус"] += 1 
    elif checking_street == True:
        answer_final_dict["Стрит"] += 1
    elif answer["Сет"] == 1:
        answer_final_dict["Сет"] += 1
    elif answer["Пары"] == 2:
        answer_final_dict["2 Пары"] += 1
    elif answer["Пары"] == 1:
        answer_final_dict["Пара"] += 1
    
    for i in list(answer_final_dict.keys()):
        if answer_final_dict[i] == 0:
            del answer_final_dict[i]

    if not bool(answer_final_dict):
        answer_final_dict = f"Старшая карта: {max(entering_numbers_int)}"

    return answer_final_dict


if __name__ == "__main__":
    entering_numbers_int = get_user_input ()
    checking_street = counting_street(entering_numbers_int)
    answer = counting_pairs_set_card (entering_numbers_int)
    print(answer_final (answer, checking_street, entering_numbers_int))