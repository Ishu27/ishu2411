import json
import sys
import requests

from st2common.runners.base_action import Action

class abc(Action):
	
	def run(self, ID, Title, Description, PageCount, Exercpt, PublishDate):
		
		try:
			response = requests.get("https://fakerestapi.azurewebsites.net/api/Books")
			print(response.status_code)
			
			print(response.url)
			print(json.loads(response))
			
		except requests.exceptions.MissingSchema:
			print("Wrong URL")
			sys.exit(0)
