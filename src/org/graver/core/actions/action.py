'''
Created on Jun 1, 2010

@author: tinyshrimp
'''


class Action:
    def __init__(self):
        if self.__class__ is Action:
            raise Exception('Cannot instantiate abstract class %s.' % self.__class__)
    
    def execute(self, evt):
        pass
    
    def getStatus(self, selectedView):
        pass