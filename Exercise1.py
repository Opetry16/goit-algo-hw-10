from pulp import LpProblem, LpMaximize, LpVariable

# Створення моделі оптимізації
model = LpProblem(name="Production_Optimization", sense=LpMaximize)

# Оголошення змінних рішення
lemonade_units = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
fruit_juice_units = LpVariable(name="Fruit_Juice_units", lowBound=0, cat="Integer")

# Додавання обмежень на ресурси
model += 2 * lemonade_units + fruit_juice_units <= 100  # Вода
model += lemonade_units <= 50  # Цукор
model += lemonade_units <= 30  # Лимонний сік
model += 2 * fruit_juice_units <= 40  # Фруктове пюре

# Додавання обмежень на виробництво
model += lemonade_units >= 0
model += fruit_juice_units >= 0

# Додавання функції максимізації
model += lemonade_units + fruit_juice_units, "Total_Production"

# Вирішення моделі
model.solve()

# Вивід результатів
print("Status:", model.status)
print("Optimal Production Plan:")
print("Lemonade units:", int(lemonade_units.value()))
print("Fruit Juice units:", int(fruit_juice_units.value()))
print("Total Production:", int(lemonade_units.value() + fruit_juice_units.value()))