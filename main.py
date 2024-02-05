import pulp

prob = pulp.LpProblem("Максимізація_виробництва_напоїв", pulp.LpMaximize)

x1 = pulp.LpVariable("Лимонад", 0, None, cat=pulp.LpContinuous)
x2 = pulp.LpVariable("Фруктовий_сік", 0, None, cat=pulp.LpContinuous)

prob += x1 + x2, "Загальна_кількість_продуктів"

prob += 2 * x1 + 1 * x2 <= 100, "Обмеження_води"
prob += 1 * x1 <= 50, "Обмеження_цукру"
prob += 1 * x1 <= 30, "Обмеження_лимонного_соку"
prob += 2 * x2 <= 40, "Обмеження_фруктового_пюре"

prob.solve()

print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Виробити 'Лимонаду': {pulp.value(x1)}")
print(f"Виробити 'Фруктовий сік': {pulp.value(x2)}")
print(f"Максимальна загальна кількість продуктів: {pulp.value(prob.objective)}")