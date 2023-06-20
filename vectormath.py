#program that does basic vector calculations in 2 dimensions(additon,dot product,cross product
#Busisiwe Michelle Ndlovu
#20/3/2023
import math

def getmag(v):
    """ this function takes two component values and returns the magnitude of their vector"""
    result= 0
    v = v.split()
    for x in v:
        x = int(x)
        result += x**2
    result = math.sqrt(result)
    #formatting for 1 decimal place
    result = "{:.1f}".format(result)
    finresult = f"Magnitude of the vector is: {result}"
    return finresult

def vectoradd(v1,v2):
    """function that adds vector values"""
    lent = len(v1)
    res1 = 0
    res2 = 0
    res3 = 0
    
    if len(v1) != len(v2):
        err = ("Error: Vectors must have the same length.")
        return err
        
    else:
        v1 = v1.split()
        v2 = v2.split()
        lent = len(v1)
        #checks for 3d vector cases
        if lent > 2:
            #adds relevantvector values
            res1 = int(v1[0])+int(v2[0])
            res2 = int(v1[1])+int(v2[1])
            res3 = int(v1[2])+int(v2[2])
            res = (res1,res2,res3)
            #tuples values to be returned 
            res = tuple(res)
            sumv = f"Sum of the vectors is: {res}"
            return sumv
            
        else:
            res1 =  int(v1[0])+int(v2[0])
            res2 = int(v1[1])+int(v2[1])   
            res = (res1,res2)
            res = tuple(res)
            sumv = f"Sum of the vectors is: {res}"           
            return sumv
            

def multiply(v,scale):
    """ multiplies vector values by scale"""
    scale = int(scale)
    v= v.split()
    #checks for 3d vector cases
    if len(v) >2:
        v1 = int(v[0])*(scale)
        v2 = int(v[1])*(scale)        
        v3 = int(v[2])*(scale)
        
        res = (v1,v2,v3)
        res = tuple(res) 
            
        prod = f"Scalar multiplication of the vector is: {res}"        
        
    else:
        v1 = int(v[0])*(scale)
        v2 = int(v[1])*(scale)
        res = (v1,v2)
        res = tuple(res) 
            
        prod = f"Scalar multiplication of the vector is: {res}"        
                 
    
    return(prod)
            
            
def dotprod(v1,v2):
    """ performs dot product of two vectors"""
    res=0
    res1=0
    res2=0
    res3=0

    if len(v1) != len(v2):
        err = "Error: Vectors must have the same length."
        return(err)
        
    else:
        v1 = v1.split()
        v2 = v2.split()
        #checks for 3d vector
        if len(v1) > 2:
            res1 =  int(v1[0])*int(v2[0])
            res2 = int(v1[1])*int(v2[1])
            res3 = int(v1[2])*int(v2[2])
            res = res1+res2+res3
            ress = f"Dot product of the vectors is: {res}"
            return ress
            
        else:
            res1 =  int(v1[0])*int(v2[0])
            res2 = int(v1[1])*int(v2[1])   
            res = res1+res2
            ress = f"Dot product of the vectors is: {res}"
            return(ress)
    
def crossprod(v1,v2):
    """ returns cross product of two vectors"""
    res1 = 0
    res2 = 0
    res3 = 0
    v1 = v1.split()
    v2 = v2.split()
    
    if len(v1) != 3 or len(v2) !=3:
        err = "Error: Vectors must have the same length and 3-dimensional."
        return(err)
    else:
        res1 = (int(v1[1])*int(v2[2]))-(int(v1[2])*int(v2[1]))
        res2 = (int(v1[2])*int(v2[0]))-(int(v1[0])*int(v2[2]))
        res3 = (int(v1[0])*int(v2[1]))-(int(v1[1])*int(v2[0]))
        res = (res1,res2,res3)
        res = tuple(res) 
        
        cprod = f"Cross product of the vectors is: {res}"
        return cprod
def main():
    optn = input("Choose an option:\n"+"1. Magnitude of a vector\n"+"2. Vector addition\n"+"3. Scalar multiplication\n"+"4. Dot product of two vectors\n"+"5. Cross product of two 3-dimensional vectors\n"+"6. Exit\n")
    while(optn != "6"):
        if optn == "1":
            v1 = input("Enter the components of the vector separated by spaces:\n")
            print(getmag(v1)) 
            
        elif optn =="2":
            v1 = input("Enter the components of the first vector separated by spaces:\n")
            v2 = input("Enter the components of the second vector separated by spaces:\n")
            print(vectoradd(v1,v2))
        elif optn == "3":
            v = input("Enter the components of the vector separated by spaces:\n")  
            scale = input("Enter the scalar:\n")
            print(multiply(v,scale))
            
        elif optn == "4":
            v1 = input("Enter the components of the first vector separated by spaces:\n")
            v2 = input("Enter the components of the second vector separated by spaces:\n")
            print(dotprod(v1,v2))
        elif optn == "5":
            v1 = input("Enter the components of the first 3-dimensional vector separated by spaces:\n")
            v2 = input("Enter the components of the second 3-dimensional vector separated by spaces:\n")
            print(crossprod(v1,v2))
        else:
            print("Invalid choice. Please choose a valid option.")
        optn =  input("Choose an option:\n"+"1. Magnitude of a vector\n"+"2. Vector addition\n"+"3. Scalar multiplication\n"+"4. Dot product of two vectors\n"+"5. Cross product of two 3-dimensional vectors\n"+"6. Exit\n")
    print("Exiting...")
  
    
if __name__ == '__main__':
        main()