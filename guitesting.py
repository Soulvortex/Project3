import json
import requests
from pprint import pprint
from sys import argv

url="http://pokeapi.co/api/v2/type/1/"
prompt = 'Enter a Number'

for i in range(1,18):
	answer=eval(input(prompt))
	if answer==2:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/1/')
		code=requests.get(new_code)
		final=code.json()
		print(json.dumps(final["damage_relations"], indent=4, sort_keys=True))
		'''
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		'''
		break
	if answer==3:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/2/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"])
		break
	if answer==4:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/4/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==5:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/5/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break	
	if answer==6:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/6/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==7:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/7/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==8:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/8/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==9:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/9/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==10:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/10/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==11:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/11/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==12:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/12/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==13:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/13/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==14:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/14/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==15:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/15/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==16:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/16/')
		code=requests.get(new_code)
		
		final=code.json()
		pprint(final)
		'''
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		'''
		break
	if answer==17:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/17/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
	if answer==18:
		new_code=str.replace(url,'http://pokeapi.co/api/v2/type/1/', 'http://pokeapi.co/api/v2/type/18/')
		code=requests.get(new_code)
		final=code.json()
		pprint(final["damage_relations"]["double_damage_from"])
		pprint(final["damage_relations"]["half_damage_from"])
		pprint(final["damage_relations"]["half_damage_to"])
		pprint(final["damage_relations"]["no_damage_from"])
		pprint(final["damage_relations"]["no_damage_to"])
		break
		
        	
















