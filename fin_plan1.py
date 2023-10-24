money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
spend_for_month = spend * increase + spend
while money_capital > 0:
   money_capital = money_capital + salary - spend_for_month
   spend_for_month = spend_for_month * increase + spend_for_month
   count += 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
