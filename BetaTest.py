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
import json
import requests
from pprint import pprint
from sys import argv

start="http://pokeapi.co/api/v2/type/1/"

class HomeScreen(Screen):
	pass
class Normal(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Fighting(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Flying(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Poison(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Ground(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Rock(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Bug(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Ghost(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Steel(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Fire(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Water(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Grass(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Psychic(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Ice(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Dragon(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Dark(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Fairy(Screen):
	code=requests.get(start)
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
	
	
	
	
	for rs in DDT:
		if DDT=="Blank":
			First="This Type Has No Super Effective Moves"
		else:
			First="Does Double Damage To: " + rs["name"]
	for rs in DDF:
		if DDF=="Blank":
			Second="This Type Does Not Take Any Super Effective Damage"
		else:
			Second="Takes Double Damage From: " + rs["name"]
	for rs in HDF:
		if HDF=="Blank":
			Third="This Type Does Not Have Any Resistances"
		else:
			Third="Take Half Damage From: " + rs["name"]
	for rs in HDT:
		if HDT=="Blank":
			Fourth="No Other Types Are Resistant To This Type"
		else:
			Fourth="Does Half Damage To: " + rs["name"]
	for rs in NDF:
		if NDF=="Blank":
			Fifth="Those Type Has No Immunities"
		else:
			Fifth="Take No Damage From: " + rs["name"]
	for rs in NDT:
		if NDT=="Blank":
			Sixth="No Other Types Are Immune To This Type"
		else:
			Sixth="Does No Damage To: " + rs["name"]
	labelText=First+'\n'+Second+'\n'+Third+'\n'+Fourth+'\n'+Fifth+'\n'+Sixth
	pass
class Change(ScreenManager):
	pass
	




class TestApp(App):
	def build(self):
		return Change()

if __name__=='__main__':		
	TestApp().run()

