import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        print(message)
        try:
            if message == 'working':
                return (True, message)
        except:
             print('Wrong Messge')
