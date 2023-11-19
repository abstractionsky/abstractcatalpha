print("Если страница не грузит, обновите ее")

import flet as ft
import requests



import socket
import hashlib

def main(page):
	page.title = "AbstractCat Interface"
	unik = ft.TextField(label="Enter text", autofocus=True)
	greetings = ft.Column()
	def iplookup(e):
		response = requests.get(url=f'http://ip-api.com/json/{unik.value}').json()
		data = f'''IP: {response.get('query')}
Int prov: {response.get('isp')}
Org: {response.get('org')}
Country: {response.get('country')}
Region name: {response.get('regionName')}
City: {response.get('city')}
Zip: {response.get('zip')}
Lat: {response.get('lat')}
Lon: {response.get('lon')}'''
		greetings.controls.append(ft.Text(f"{data}"))
		unik.value = ""
		page.update()
		unik.focus()

	def hostname2ip(e):
		greetings.controls.append(ft.Text(f"{socket.gethostbyname(unik.value)}"))
		unik.value = ""
		page.update()
		unik.focus()

	def txt2md5click(e):
		greetings.controls.append(ft.Text(f"{hashlib.md5(unik.value.encode()).hexdigest()}"))
		unik.value = ""
		page.update()
		unik.focus()

	def numberlookup(e):
		response = requests.get(f"https://mobile-location.org/emulator/check?driver=geo&country=RU&provider=phone&uid=+{unik.value}&mode=undefined&_=1698494081981").json()
		greetings.controls.append(ft.Text(f"{response}"))
		unik.value = ""
		page.update()
		unik.focus()


	page.add(
		unik,
		ft.ElevatedButton("IP Lookup", on_click=iplookup),
		ft.ElevatedButton("Number Lookup", on_click=numberlookup),
		ft.ElevatedButton("Hostname2Ip", on_click=hostname2ip),
		ft.ElevatedButton("Txt2Md5", on_click=txt2md5click),
		greetings,
	)

ft.app(target=main, view=ft.WEB_BROWSER)