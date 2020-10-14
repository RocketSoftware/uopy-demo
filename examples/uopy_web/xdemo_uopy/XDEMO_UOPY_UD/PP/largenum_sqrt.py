################################################
# Copyright (C) Rocket Software 1993-2015
from decimal import * 
getcontext().prec = 64 

def getsqrt( num ):
    num = Decimal(num)
    d = num**Decimal('.5')
    return str(d)
#################################################
