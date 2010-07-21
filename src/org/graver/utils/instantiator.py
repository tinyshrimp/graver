'''
Created on Jun 2, 2010

@author: tinyshrimp
'''

def createClassInstance(cls):
    if cls is None or '' == cls:
        return None
    
    modulePath, classname = cls.split(':')
    
    if modulePath is None or '' == modulePath:
        return None
        
    if classname is None or '' == classname:
        return None
    
    module = createModuleInstance(modulePath)        
    if module is None:
        return None

    try:
        return getattr(module, classname)
    except:
        return None
    
def createModuleInstance(module):
    if module is None or '' == module:
        return None
    
    mod = None
    
    try:
        mod = __import__(module)
    except:
        return None
    
    if mod is None:
        return None
    
    attrs = module.split('.')
    
    try:
        for attr in attrs[1:]:
            mod = getattr(mod, attr)
        return mod
    except:
        return None