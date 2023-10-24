salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
spend_for_month = spend * increase + spend
months = 1
itog = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while months != 10:
        money_capital = salary - spend_for_month
        spend_for_month = spend_for_month * increase + spend_for_month
        itog = itog + money_capital
        months += 1
itog = round((itog -1000) * -1)   # потому что первый месяц без повышения цены.
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", itog)
