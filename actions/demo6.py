import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
        def run(self,id,title,desc,pagecount,excerpt,pubdate):
                try:
                    
              		      x={"ID": id}
                	      y=json.dumps(x)
			                  headers={'content-type': 'application/json'}
			                  url='https://fakerestapi.azurewebsites.net/api/Books'
			                  res=requests.get(url,headers=headers,data=y)
			                  print(res)
			                  z=res.json()
			                  print(z)
			

	              except:
                    	  sys.exit(0)
