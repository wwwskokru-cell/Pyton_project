'''
Дополните функцию, которая принимает строковый параметр и переворачивает каждое слово в строке. Все пробелы в строке должны быть сохранены.

Примеры
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    #text = text.split(' ')
    return ' '.join([i[::-1] for i in text.split(' ')])

print(reverse_words("This is an example!"))
