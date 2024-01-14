from random import randint

def paradox(set_doors_value):
    """Проверяет теорию Монти Холла с тремя дверьми."""
    # Создаёт список из заданного кол-ва наборов дверей.
    arr_doors = [[0, 0 ,0] for x in range(set_doors_value)]
    # Рандомной двери во всех списках присваивается "х" (приз).
    for set_doors in arr_doors:
        prize_door = randint(0, 2)
        set_doors[prize_door] = 'x'

    # Счётчики для отслеживания кол-ва верно и неверно угаданных дверей.
    right_choice = 0
    bad_choice = 0

    # Определяет рандомно выбранную дверь в каждом наборе,
    # присваивая ей единицу в качестве указания выбора.
    # Подсчитывает верно и неверно угаданные двери.
    for set_doors in arr_doors:
        chosen_door = randint(0, 2)
        if set_doors[chosen_door] != 'x':
            set_doors[chosen_door] = 1
        if set_doors[chosen_door] == 'x':
            right_choice += 1
        else:
            bad_choice += 1
    
    print_messages(right_choice, bad_choice, set_doors_value)

    # Сбрасывает значения счётчиков.
    right_choice = 0
    bad_choice = 0

    # Убирает одну пустую дверь и меняет выбранную дверь на другую.
    for set_doors in arr_doors:
        set_doors.remove(0)
        try:
            chosen_door_index = set_doors.index(1)
        except ValueError:
            chosen_door_index = set_doors.index('x')
        if chosen_door_index == 0:
            new_choise = 1
        else:
            new_choise = 0
        if set_doors[new_choise] == 'x':
            right_choice += 1
        else:
            bad_choice += 1
    
    return right_choice, bad_choice, set_doors_value, True

def print_messages(right_choice, bad_choice, set_doors_value, flag=False):
        """Выводит сообщения и информацию со счётчиков."""
        if flag:
            right_percent = right_choice / set_doors_value * 100
            bad_percent = bad_choice / set_doors_value * 100
            print("Если бы сменили выбранную дверь:")
            print(f'\tВерно угаданных дверей: {right_choice}, что составляет {right_percent}%')
            if right_choice > bad_choice:
                difference = right_percent - bad_percent
                print(f'\nШанс выигрыша после смены выбранной двери возрос на {difference}%')
        else:
            right_percent = right_choice / set_doors_value * 100
            bad_percent = bad_choice / set_doors_value * 100
            print('Если остаться при своём первоначальном выборе:')
            print(f'\tВерно угаданных дверей - {right_choice}, что составляет {right_percent}%')
            print(f'\tНеверно угаданных дверей - {bad_choice}, что составляет {bad_percent}%\n')

if __name__ == '__main__':
    print_messages(*paradox(int(input('Введите желаемое кол-во наборов дверей для теста: '))))
