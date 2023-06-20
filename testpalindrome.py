#Doctest for palindrome.py module function "is_palindrome()" that checks 5 path coverage test cases
#Busisiwe Michelle Ndlovu
#19/4/2023

#test values are followed by their expected results

"""
>>> import palindrome
>>> palindrome.is_palindrome("a")
True
>>> palindrome.is_palindrome("aba")
True
>>> palindrome.is_palindrome("acd")
False
>>> palindrome.is_palindrome("")
True
>>> palindrome.is_palindrome("rac e car")
True

"""
import doctest
doctest.testmod(verbose=true)
