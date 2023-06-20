# Checks if the sum of a number's proper divisors is equal to the number itself (perfect number)

# Busisiwe Michelle Ndlovu

# 6/3/2023
num = eval(input("Enter a number: \n"))

divSum = 0 #this value holds the sum of the proper divisors
#the following lines check if the abover entered number is a positive integer since a perfect number has to be positive
if num <= 0:
    print(f"{num} is not a perfect number.")
else:
    print("The proper divisors of",num,"are:")
    #The for loop below checks for the remainder after division of the entered number and values from 1 to that number.
    for x in range(1,num):
        if (num % x) > 0:#if the divisor isnt proper, it passes to the next value
            pass
        else:#if the value is a proper divisor, it is printed and added to the sum of proper divisors
            print(x,end =" ")
            divSum += x
    print("\n")
    if divSum == num:#if the sum of proper divisors equals the entered value, it is a perfect number
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")