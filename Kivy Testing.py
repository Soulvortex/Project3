import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TypesScreen(GridLayout):
	def __init__(self, **kwargs):
		super(TypesScreen, self).__init__(**kwargs)
		self.cols = 6
		self.add_widget(Button(text='Normal'))
		self.add_widget(Button(text='Fighting'))
		self.add_widget(Button(text='Flying'))
		self.add_widget(Button(text='Poison'))
		self.add_widget(Button(text='Ground'))
		self.add_widget(Button(text='Rock'))
		self.add_widget(Button(text='Bug'))
		self.add_widget(Button(text='Ghost'))
		self.add_widget(Button(text='Steel'))
		self.add_widget(Button(text='Fire'))
		self.add_widget(Button(text='Water'))
		self.add_widget(Button(text='Grass'))
		self.add_widget(Button(text='Electric'))
		self.add_widget(Button(text='Psychic'))
		self.add_widget(Button(text='Ice'))
		self.add_widget(Button(text='Dragon'))
		self.add_widget(Button(text='Dark'))
		self.add_widget(Button(text='Fairy'))
		


class Pokemon(App):
	def build(self):
		#return Label(text='Welcome to Pokemon Typing Calculator!')
		return TypesScreen

		
if __name__== '__main__':
	Pokemon().run()