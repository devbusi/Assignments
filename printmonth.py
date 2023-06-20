#program thhat takes a month,and its start day(sun,mon,etc) and prints it's calendar in a 6x7 grid
#Busisiwe Michelle Ndlovu
#16/3/23

mon = input("Enter the name of a month (e.g. January, ..., December):\n")

day = eval(input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n"))

date = 1 #date throughout the month


months =["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
count = 0

for n in range(12):
  #checks if month is valid
  if months[n] == mon.upper():
    count = 1
if count < 1 or ((day < 1 or day > 7)):
  print("Invalid calendar: you have either entered an incorrect month name or start day.")
  quit()

   
print(mon)

week=["Mo","Tu","We","Th","Fr","Sa","Su"]


#for rows
for x in range(0,7):
  #for columns
  for i in range(0,7):
    #for februarys 28 day case
    if mon.upper() == "FEBRUARY":
      if date == 29:
        break
    #to cut off at 31
    elif ((mon.upper() == "JANUARY") or  (mon.upper() == "MARCH") or  (mon.upper() == "MAY") or ( mon.upper() == "JULY") or  (mon.upper() == "AUGUST") or  (mon.upper() == "OCTOBER") or ( mon.upper() == "DECEMBER")):
      if date == 32:
        break    
        #to cut off date at 30
    elif  date == 31:
        break
    #prints days of the week
    if  x == 0 :        
      print(week[i],end =" ")
      #prints spaces for month of feburary
    elif x ==1 and  mon.upper() == "FEBRUARY":
      print("", end =" ")
      continue
    #prints spaces befor start day
    elif x == 1 and (day-1) > 0:
      print("  ",end =" ")
      day=day-1
      #prints remaining dates after spaces on starting line
    elif x == 1:
      print("",date,end =" ")
      date = date+1
      #adds spaces befor single digit numbers for allignment
    elif date>=0 and date<10:
      print("",date,end =" ")
      date+=1
      #prints remaining numbers
    else:
      print(date, end =" ")
      date+=1
  print()
  
          
