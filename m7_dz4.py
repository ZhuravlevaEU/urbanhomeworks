# Форматирование строк
# 1_Использование метода %
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников %s' % team1_num)
print('В команде Мастера кода участников %s, в команде Волшебники данных %s' % (team1_num, team2_num))

# 2_Использование метода format()
score_1 = 40
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Команды решили {} и {} задач.'.format((score_2), (score_2)))

team1_time = 1552.512
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

# 3_Использование f строки
print(f'Команды решили {score_1} и {score_2} задач.')

tasks_total = 82 # количество решенных задач
time_avg = 45.2 # среднее время решения

print(f"Результат битвы: победа команды Мастера кода!")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = 'Победа команды Волшебники данных!'
print (f"Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time + team2_time) / 2} "
       f"секунды на задачу!.")




