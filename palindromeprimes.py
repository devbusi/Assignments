# this program uses recursive functions to find all palindromic primes between two integers N, M, supplied as input
#Busisiwe Michelle Ndlovu
#25/4/2023
import sys
sys.setrecursionlimit (30000)

def reverse(num):
    """ this function takes a string and returns its reverse using recursion"""
    num = str(num)
    #base case of string length equal to zero
    if len(num) == 0:
        return ""
    else:
        return num[-1] + reverse(num[:-1])
                 
        
def isprime(N,i=2):
    """ this function checks wether a value is prime or not recursively"""
    #base case of value equal to the iterating value
    if N == i:
            return True
    elif N % i == 0:
        return False
    return isprime(N,i+1)  
     
    
def ispalindromic(N,M):
    """ this function uses recursive functions to find all palindromic primes between two integers N, M, supplied as input"""
    #base case of reaching ending value or beginning value lower than ending value
    if N > M or N > M:
        return
    #checks if the inputted value is palindromic""
    elif N == int(reverse(N)):
        #checks wether the reversed number is prime value or not"""
        if(isprime(N)):
            #prints the value and continues recursion 
            print(N)
        return(ispalindromic(N+1,M))
    else:
        #continues recursively if the value isnt prime, or isnt palindromic
        return(ispalindromic(N+1,M))
def main():
    N =  eval(input("Enter the starting point N:\n"))
    M =  eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    ispalindromic(N,M)
    
if __name__ == "__main__":
    main()
