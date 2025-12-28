# Program to check whether a student has passed or failed

maths = int(input("Enter your marks of maths (out of 100) : "))

chem = int(input("Enter your marks of chemistry (out of 100) : "))

phy = int(input("Enter your marks of physics (out of 100) : "))

total_percentage = 100*(maths+chem+phy)/300
if(maths<33):
    print("Sorry you are failed! and your total is : ",total_percentage,"%")
    

elif(chem<33):
    print("Sorry you are failed! and your total is : ",total_percentage,"%")
    

elif(phy<33):
    print("Sorry you are failed! and your total is : ",total_percentage,"%")
    
elif(total_percentage<40):
    print("Sorry you are failed! and your total is : ",total_percentage,"%")

elif():
    print("Your have passed and your total is : ",total_percentage,"%")

    