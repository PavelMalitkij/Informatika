list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2#Определяем общ. кол-во игроков и находим индекс для разделения

#Делим на команды
first_team = list_players[:middle_index]#первая
second_team = list_players[middle_index:]#вторая

print(first_team)
print(second_team)
