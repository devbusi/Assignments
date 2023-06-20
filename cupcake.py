# The following program asks a number of questions to determine wether a food shoould be eaten or not after being dropped

# Busisiwe Michelle Ndlovu

# 6/3/2023

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
#the first question is asked
q1 = input("Did anyone see you? (yes/no)\n")
if q1 == "yes":
    #r stands for right, so q2r = question 2 on the right branch
    q1r = input("Was it a boss/lover/parent? (yes/no)\n")
    if q1r == "no":
        print("Decision: Eat it.")
    else:
        q2r =input("Was it expensive? (yes/no)\n")#question 2 on the right branch
        if q2r =="yes":
            q3ry= input("Can you cut off the part that touched the floor? (yes/no)\n")#questopn 3 on the right if the previous answer(q2r) was yes
            if q3ry == "yes":
                print("Decision: Eat it.")         
            else:
                print("Decision: Your call.")
        else:
            q3rn = input("Is it chocolate? (yes/no)\n")#questopn 3 on the right if the previous answer(q2r) was no
            if q3rn == "yes":
                print("Decision: Eat it.")     
            else:
                print("Decision: Don't eat it.")
else:#commences branch on the left of the first quetsion
    qa = input("Was it sticky? (yes/no)\n")#questions are in alphabetical order for the left wing
    if qa == "yes":
        qb = input("Is it a raw steak? (yes/no)\n")
        if qb == "yes":
            qc = input("Are you a puma? (yes/no)\n")
            if qc == "no":
                print("Decision: Don't eat it.")
            else:                
                print("Decision: Eat it.") 
        else:
            qd = input("Did the cat lick it? (yes/no)\n")
            if qd == "yes":
                qe = input("Is your cat healthy? (yes/no)\n")
                if qe == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        qf = input("Is it an Emausaurus? (yes/no)\n")
        if qf == "no":
            qd1 = input("Did the cat lick it? (yes/no)\n")#repetition of previous branch questiosn is followed by 1
            if qd1 == "yes":
                qe1 = input("Is your cat healthy? (yes/no)\n")
                if qe1 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
        else:
            qg = input("Are you a Megalosaurus? (yes/no)\n")
            if qg == "no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
        
    
