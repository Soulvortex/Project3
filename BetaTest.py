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
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
import json
import requests
from pprint import pprint
from sys import argv

start="http://pokeapi.co/api/v2/type/1/"
#HomeScreen Where We Set all of the Buttons, a lot of this is declared in the KV file
class HomeScreen(Screen):
	pass
#Ok now all these classes contain the same parsing material but I will only comment normal
class Normal(Screen):
	code=requests.get(start)
	final=code.json()
	#So above we make the api call and turn the data into a nicer easier to parse json object
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	#Above here we go through 6 instances of damage relations, check to see if they are empty (if they are set to blank) and then store it in another file to parse again
	
	#Below is all of the for loops that do the second parse, if "blank" then we return a statement saying so, else we pull out "name" out of the variables such as DDT which will return 1 of the 18 types
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	#finally our kv file calls to this statement in each screen and the label = combinations of all the statements
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Fighting(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/2/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
			
	
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Flying(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/3/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Poison(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/4/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Ground(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/5/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Rock(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/6/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Bug(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/7/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Ghost(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/8/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Steel(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/9/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Fire(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/10/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Water(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/11/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Grass(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/12/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Electric(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/13/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Psychic(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/14/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class dragon(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/16/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Ice(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/15/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Dark(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/17/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass
class Fairy(Screen):
	new_code=str.replace(start, 'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/18/')
	code=requests.get(new_code)
	final=code.json()
	if final["damage_relations"]["double_damage_to"]==[]:
		DDT="Blank"
	else:
		DDT=final["damage_relations"]["double_damage_to"]
	if final["damage_relations"]["double_damage_from"]==[]:
		DDF="Blank"
	else:
		DDF=final["damage_relations"]["double_damage_from"]
	if final["damage_relations"]["half_damage_from"]==[]:
		HDF="Blank"
	else:
		HDF=final["damage_relations"]["half_damage_from"]
	if final["damage_relations"]["half_damage_to"]==[]:
		HDT="Blank"
	else:
		HDT=final["damage_relations"]["half_damage_to"]
	if final["damage_relations"]["no_damage_from"]==[]:
		NDF="Blank"
	else:
		NDF=final["damage_relations"]["no_damage_from"]
	if final["damage_relations"]["no_damage_to"]==[]:
		NDT="Blank"
	else:
		NDT=final["damage_relations"]["no_damage_to"]
	
	
	
	if DDT=="Blank":
		First="This Type Has No Super Effective Moves"
	else:
		First="Does Double Damage To"
		for rs in DDT:
			First=First+", "+rs["name"]
			
	if DDF=="Blank":
		Second="This Type Does Not Take Any Super Effective Damage"
	else:
		Second="Takes Double Damage From"
		for rs in DDF:
			Second=Second+", " + rs["name"]
	
	if HDF=="Blank":
		Third="This Type Does Not Have Any Resistances"
	else:
		Third="Take Half Damage From"
		for rs in HDF:
			Third=Third+", "+rs["name"]
	
	if HDT=="Blank":
		Four="No Other Types Are Resistant To This Type"
	else:
		Four="Does Half Damage To" 
		for rs in HDT:
			Four=Four+", "+rs["name"]
			
	if NDF=="Blank":
		Fifth="This Type Has No Immunities"
	else:
		Fifth="Take No Damage From"
		for rs in NDF:
			Fifth=Fifth+", "+rs["name"]
	
	if NDT=="Blank":
		Sixth="No Other Types Are Immune To This Type"
	else:
		Sixth="Does No Damage To"
		for rs in HDT:
			Sixth=Sixth+", "+rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Four+'\n'+Fifth+'\n'+Sixth
	pass		
class Change(ScreenManager):
	pass	



#Finally we build everything in the app, we call back change which is our screen manager
#the screen manager contains every screen (19 of them) and can be called in one simple call
#we also add music that loops through the program
class TestApp(App):
	def build(self):
		sound=SoundLoader.load('pokemusic.mp3')
		sound.loop=True
		sound.play()
		return Change()
	
		
#this simply runs the app
#If you want an explanation of the Kv file it is very hard to explain
#and would be easier to explain in person
#but to try to simplify the kv is sort of an html type of programming language
#we put all of our widgets in there and by inputting their class name in the py file we simply put "pass" and all the info is passed from the kv to the py file
if __name__=='__main__':		
	TestApp().run()

