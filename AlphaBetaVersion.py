import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class ScreenOne(Screen):
	def __init__(self,**kwargs):
		super(ScreenOne, self).__init__(self, **kwargs)
		firstbox = GridLayout(cols=6)
		label= Label(text='Please Select The Type of Pokemon', font_size='24dp')
		button1=(Button(text='Normal'))
		button1.bind(on_press=self.changer)
		button2=(Button(text='Fighting'))
		button2.bind(on_press=self.changer)
		button3=(Button(text='Flying'))
		button3.bind(on_press=self.changer)
		button4=(Button(text='Poison'))
		button4.bind(on_press=self.changer)
		button5=(Button(text='Ground'))
		button5.bind(on_press=self.changer)
		button6=(Button(text='Rock'))
		button6.bind(on_press=self.changer)
		button7=(Button(text='Bug'))
		button7.bind(on_press=self.changer)
		button8=(Button(text='Ghost'))
		button8.bind(on_press=self.changer)
		button9=(Button(text='Steel'))
		button9.bind(on_press=self.changer)
		button10=(Button(text='Fire'))
		button10.bind(on_press=self.changer)
		button11=(Button(text='Water'))
		button11.bind(on_press=self.changer)
		button12=(Button(text='Grass'))
		button12.bind(on_press=self.changer)
		button13=(Button(text='Electric'))
		button13.bind(on_press=self.changer)
		button14=(Button(text='Psychic'))
		button14.bind(on_press=self.changer)
		button15=(Button(text='Ice'))
		button15.bind(on_press=self.changer)
		button16=(Button(text='Dragon'))
		button16.bind(on_press=self.changer)
		button17=(Button(text='Dark'))
		button17.bind(on_press=self.changer)
		button18=(Button(text='Fairy'))
		button18.bind(on_press=self.changer)
		firstbox.add_widget(label)
		firstbox.add_widget(button1)
		self.add_widget(firstbox)
		
	def changer(self,*args):
		self.manager.current='screen2'
			
class ScreenTwo(Screen):
	def __init__(self,**kwargs):
		super(ScreenTwo,self).__init__(self, **kwargs)
		box2=GridLayout(cols=2)
		label2=Label(text="BlahBlah", font_size='24dp')
		return_button=Button(text="Return to Screen", size_hint_y=None, size_y=100)
		return_button.bind(on_press=self.changer)
		box2.add_widget(return_button)
		box2.add_widget(label2)
		self.add_widget(box2)
		
	def changer(self,*args):
		self.manager.current='screen1'

class Pokemon(App):
	def build(self):
		my_screenmanager = ScreenManager()
		screen1=ScreenOne(name='screen1')
		screen2=ScreenTwo(name='screen2')
		my_screenmanager.add_widget(screen1)
		my_screenmanager.add_widget(screen2)
		return my_screenmanager
		
if __name__ == '__main__':
	Pokemon().run()
	
		
		
		
		
