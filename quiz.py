def challenge(quiz):
    answer = input(f'{quiz[0]}: ')
    if answer == quiz[1]:
        return True
    return False


quiz_list = [['1+1=?', '2'], ['Moon in German?', 'Mond'], ['H2O?', 'Water']]
points = 0

for quiz_item in quiz_list:
    if challenge(quiz_item):
        points += 1

print(f'You got {points} questions right!')
