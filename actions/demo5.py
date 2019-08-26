import json
import sys
import requests

from st2common.runners.base_action import Action

class abc(Action):
	
	def run(self,id,title,descrp,pgcnt,exercpt,publishdate):
		
		try:
			x = {"ID": id, "Title":title, "Description":descrp, "PageCount":pgcent ,"Excerpt":exercpt, "PublishDate":publishdate}
			response = requests.post("https://fakerestapi.azurewebsites.net/api/Books")
			print(response.status_code)
			
			
			print(json.dumps(response))
			
		except requests.exceptions.MissingSchema:
			print("Wrong URL")
			sys.exit(0)
