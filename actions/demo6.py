import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
        def run(self,id):
                try:              	
			id1=str(id)
			headers={'content-type': 'application/json'}
			url='https://fakerestapi.azurewebsites.net/api/Books/'+id1
			res=requests.get(url,headers=headers)		
			z=res.json()
			print(z)
			
		except:
                    	sys.exit(0)
