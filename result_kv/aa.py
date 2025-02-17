import os
import openpyxl
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class Interface(GridLayout):
    adress_a = StringProperty("")
    adress_b = StringProperty("")

    def on_a_text(self, instance, value):
        self.adress_a = value
        print(f"Address A: {self.adress_a}")

    def on_b_text(self, instance, value):
        self.adress_b = value
        print(f"Address B: {self.adress_b}")

    def excel(self):
        try:
            # Импорт книги в двух экземплярах - с формулами и с их вычисленными результатами
            wb_formula = openpyxl.load_workbook(filename='x.xlsx')
            wb_data = openpyxl.load_workbook(filename='x.xlsx', data_only=True)

            # Импорт активного листа книги
            data = wb_data.active
            result = wb_formula.active

            # Извлекаем данные из книги без формул, простое число a и результат формулы b
            a = data[self.adress_a].value
            b = data[self.adress_b].value

            # Проводим вычисления и записываем в столбец
            result["A5"] = a + b

            # Сохраняем в книгу с формулами - так мы их не теряем
            wb_formula.save('test.xlsx')
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

class MyApp(App):
    def build(self):
        return Interface()

if __name__ == '__main__':
    MyApp().run()

