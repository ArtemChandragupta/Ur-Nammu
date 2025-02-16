import openpyxl

# Импорт книги в двух экземплярах - с формулами и с их вычисленными результатами
wb_formula = openpyxl.load_workbook(filename='x.xlsx')
wb_data    = openpyxl.load_workbook(filename='x.xlsx', data_only=True)

# Импорт активного листа книги
data   = wb_data.active
result = wb_formula.active

# Извлекаем данные из книги без формул, простое число a и результат формулы b
a = data["A1"].value
b = data["C3"].value

# Проводим вычисления и записываем в столбец
result["A5"] = a + b

# Сохраняем в книгу с формулами - так мы их не теряем
wb_formula.save('test.xlsx')
