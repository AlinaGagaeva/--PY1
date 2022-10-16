salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

for delta in range(0, months):
    delta = spend - salary
    spend = spend * (1+increase)
    need_money += delta
print(round(need_money))
