import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
        def run(self,id):
                try:
			x={"ID": id}
                	y=json.dumps(x["id"])
			headers={'content-type': 'application/json'}
			url='https://fakerestapi.azurewebsites.net/api/Books'
			res=requests.get(url,headers=headers,data=y)
		
			z=res.json()
			print(z)
			
		except:
                    	 sys.exit(0)
