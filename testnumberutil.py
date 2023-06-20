import math
#Doctest script that achieves 8 coverage paths for the aswords function
#Busisiwe Michelle Ndlovu
#17/4/2023

#numberutil.py with function aswords that returns english text of number
#function input is followed by the expected result
"""
>>> import numberutil
>>> numberutil.aswords(900) 
'nine hundred'
>>> numberutil.aswords(920)
'nine hundred and twenty'
>>> numberutil.aswords(950)
'nine hundred and fifty'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(73)
'seventy three'
>>> numberutil.aswords(70)
'seventy'
>>> numberutil.aswords(20)
'twenty'
>>> numberutil.aswords(173)
'one hundred and seventy three'

"""
import doctest
doctest.testmod(verbose=true)