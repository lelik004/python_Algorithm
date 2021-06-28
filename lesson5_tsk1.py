"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
import collections
import random

n = int(input('Введите количество предприятий: '))
Companies = collections.namedtuple('Company', 'name company_profit')
company_lst = []
company_profit = 0
total_profit = 0

for company_count in range(1, n + 1):
    name = input(f'Введите наименование компании {company_count}: ')
    print(f'Введите прибыль предприятия {name}.')
    for quarter in range(1, 5):
        # quarter_profit = random.randint(0, 1000)
        # print(f'Профит компании {name} за квартал {quarter}: {quarter_profit}')
        # company_profit += quarter_profit
        company_profit += int(input(f'Профит компании {name} за квартал {quarter}: '))
    company = Companies(name, company_profit)
    company_lst.append(company)
    total_profit += company_profit
    company_profit = 0

print(f'Средняя прибыль всех предприятий за год: {total_profit / n}')

for company in company_lst:
    if company.company_profit > (total_profit / n):
        print(f'Прибыль предприятия "{company.name}" выше среднего и равна {company.company_profit}')
    elif company.company_profit < (total_profit / n):
        print(f'Прибыль предприятия "{company.name}" ниже среднего и равна {company.company_profit}')
    else:
        print(f'Прибыль предприятия "{company.name}" равна средней прибыли и равна {company.company_profit}')
