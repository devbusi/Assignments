# this program assists with debugging python programs by  insert a trace statement at the beginning of each function definition or removing them if a program already contains them
#Busisiwe Michelle Ndlovu
# 12/5/2023

print("***** Program Trace Utility *****")
filename = str(input("Enter the name of the program file: "))
array = []
#test case
try:
    file_test = open(filename, "r", encoding = "utf-8")
    
    for line in file_test:
        array.append(line.strip("\n"))
    file_test.close()

#for ioerror accomodation
except IOError as error:
    print(error)
#removes debug
if '"""DEBUG"""' in array1[0]:
    for j in array:
        if '"""DEBUG"""' in j:
            array.remove(j)
else:
    #adds debug
    array.insert(0, '"""DEBUG"""')
    for x in range(1,len(array)):
        if "def" in array[x]:
            old = array[x]
            new = old[4:old.index("("):]
            array.insert(x + 1,'    """DEBUG""";' +"print('"+new+"')")

try:
    file_test = open(filename,"w",encoding = "utf-8")
    
    for y in array1:
        file_test.writelines(y + "\n")
        
    file_test.close()
    print("success")
    
except:
    print("there was an error")