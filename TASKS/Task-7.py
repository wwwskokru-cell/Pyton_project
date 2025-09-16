'''
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список элементов без элементов с одинаковым значением, стоящих рядом друг с другом, и сохраняя исходный порядок элементов.

Например:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''
#не решена

def unique_in_order(sequence):
    if sequence == None:
        return []
    sequence = list(sequence)
    if len(sequence) == 1:
        return sequence
    sequence_answer = []
    for i in sequence[1:]:
        if i != sequence[sequence.index(i) - 1]:
            sequence_answer.append(i)

    sequence = sequence_answer
    return sequence 
