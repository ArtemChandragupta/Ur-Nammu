import os
import openpyxl

from kivy.app            import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label      import Label
from kivy.uix.button     import Button
from kivy.uix.textinput  import TextInput
from kivy.properties     import StringProperty

class Interface(GridLayout):
    adress_a = StringProperty("")
    adress_b = StringProperty("")

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.cols = 2

        # Кнопка активации
        self.btn1 = Button(text='Touch xlsx')
        self.btn1.bind(on_press=self.excel)
        self.add_widget(self.btn1)

        self.add_widget(Label(text='Address A:'))
        self.input_a = TextInput(multiline=False)
        self.input_a.bind(text=self.on_a_text)
        self.add_widget(self.input_a)

        self.add_widget(Label(text='Address B:'))
        self.input_b = TextInput(multiline=False)
        self.input_b.bind(text=self.on_b_text)
        self.add_widget(self.input_b)

    def on_a_text(self, instance, value):
        self.adress_a = value

    def on_b_text(self, instance, value):
        self.adress_b = value

    def excel(self, instance):
        try:
            # Импорт книги в двух экземплярах - с формулами и с их вычисленными результатами
            wb_formula = openpyxl.load_workbook(filename='x.xlsx')
            wb_data    = openpyxl.load_workbook(filename='x.xlsx', data_only=True)

            # Импорт активного листа книги
            data   = wb_data.active
            result = wb_formula.active

            # Извлекаем данные из книги без формул, простое число a и результат формулы b
            a = data[self.adress_a].value # A1
            b = data[self.adress_b].value # C3

            # Проводим вычисления и записываем в столбец
            result[self.adress_result] = a + b

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
