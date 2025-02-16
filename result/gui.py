from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os

def callback(instance):
    os.system('notify-send GITLER')

btn1 = Button(text='Hello world 1')
btn1.bind(on_press=callback)

class Interface(GridLayout):

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.add_widget(Button(text='Hello world', font_size=14))
        self.add_widget(btn1)
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return Interface()


if __name__ == '__main__':
    MyApp().run()

