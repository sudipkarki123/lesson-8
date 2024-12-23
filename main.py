# medicalcause=input("do you have medical cause? Press N for 'NO' and press Y for 'Yes':") 
# if medicalcause=='Y':
#     print("you are allowed to write exam") 
# elif medicalcause=='N':
#     attendance=int(input("Enter your attendance percentage:"))
#     if attendance>75:
#         print("You are allowed to write exam")
#     else:
#         print("You are not allowed to write exam")
# else:
#     print("Invalid input")

# uc=int(input("Enter the units consumed by you:"))
# if uc<50:
#     amt=uc*2.60+25
# elif uc>50 and uc<100:
#     amt=uc*3.25+35
# elif uc>100 and uc<200:
#     amt=uc*5.26+45
# else:
#     amt=uc*8.45+75
# print("Amount need to be paid:",amt)

print("Select your ride: ")
print("1. Bike")
print("2. Car")
#take input of number 1 or 2
#select your ride
choice = int( input("Enter your choice: ") )
#User entering option 1
if( choice == 1 ): #condition 1 outer if statement
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")
  choice2=int(input("Enter you choice2: "))
  if choice2==1: #inner if statement
    print("you have selected scooty")
  else:
    print("you have selected scooter")

#User entering option 2
elif( choice == 2 ): #outer elif statement
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  choice3=int(input("enter your choice3: "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected sedan")
  else:
    print("you have selected XUV")

else: #outer else statement
  print("Wrong choice!")
