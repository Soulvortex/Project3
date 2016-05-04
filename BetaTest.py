import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.widget import Widget



class FirstScreen(Screen):
	pass
class SecondScreen(Screen):
	pass
class Change(ScreenManager):
	pass




class TestApp(App):
	def build(self):
		return Change()

if __name__=='__main__':		
	TestApp().run()

