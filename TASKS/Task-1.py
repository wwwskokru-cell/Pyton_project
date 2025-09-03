'''
Задача: нужно вывести победные комбинации в покере по цифрам 1-13
'''
entering_numbers = input("Введите 5 чисел через запятую от 1 до 13: ").lower().strip()
entering_numbers_list = entering_numbers.split(",")
entering_numbers_int = []
for i in entering_numbers_list:
    i = int(i)
    entering_numbers_int.append(i)
answer = {
    "Пары" : 0,
    "Сет" : 0,
    "Карэ" : 0
}
_ = 1
number_of_cards ={}
while _ < 14:
    number_of_cards [_]=entering_numbers_int.count(_)
    if number_of_cards [_] == 0:
        del number_of_cards[_]
    elif number_of_cards [_] == 2:
        answer["Пары"] += 1
    elif number_of_cards [_] == 3:
        answer["Сет"] += 1
    elif number_of_cards [_] == 4:
        answer["Карэ"] += 1
    _+=1

print(answer)

    

