user_answer = int(input('Введите число 1-12: '))
c = ['Вы ввели некоректный месяц', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
     'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
d = {'Вы ввели некоректный месяц' 'Январь' 'Февраль' 'Декабрь': 'Зима',
     'Март' 'Апрель' 'Май': 'Весна',
     'Июнь' 'Июль' 'Август': 'Лето',
     'Сентябрь''Октябрь''Ноябрь': 'Осень'}
print(c[user_answer] + ' Относится к времени года: ' + (d[user_answer]))
