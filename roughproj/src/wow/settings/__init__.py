from .default import *

try:
    from .local import *
    deployed = False 
except: 
    deployed = True
if deployed == True: 
    from .deploy import * 