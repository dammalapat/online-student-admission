import random
import time

def admission():
    print("\t\t\t\t\t\t YOU HAVE CHOSEN TO TAKE ADMISSION IN THIS COLLEGE ")
    name=input("enter the student's name :")
    gender=input("enter the student's gender :")
    DOB=input("enter DOB as a string by giving hyphens :")
    address=input("enter the student's address :")
    pincode=input("enter your village pincode :")
    guardian_name=input("enter guardian's name :")
    number=input("enter your mobile number :")
    print("\t\t\t\t\t\t THERE WILL BE AN EXAM TO JOIN INTO THIS COLLEGE")
    print("TOTAL 10 QUESTIONS")
    print("press ENTER to start the quiz")
    e=input()
    startTime=time.time()
    list1=['+','-','*','//','%',]
    questions=0
    score=0
    while(questions!=10):
        value1=random.randint(11,20)
        value2=random.randint(1,10)
        arthmatic=random.choice(list1)
        print(value1, arthmatic , value2)
        if(arthmatic=='+'):
            answer=(value1)+(value2)
        elif(arthmatic=='-'):
            answer=(value1)-(value2)
        elif(arthmatic=='*'):
            answer=(value1)*(value2)
        elif(arthmatic=='//'):
            answer=(value1)//(value2)
        elif(arthmatic=='%'):
            answer=(value1)%(value2)
        user_answer=int(input("enter your answer :"))
        if(answer==user_answer):
            score+=1
        questions+=1
    endTime=time.time()
    totalTime=endTime-startTime
    print(" YOUR TOTAL SCORE IS :",score)
    print(" TOTAL TIME TAKEN FOR YOU TO COMPLETE THE QUIZ IS :",int(totalTime),"seconds")
    totalTime=int(totalTime)
    if(score < 6 or totalTime > 60):
        print(" \t\t\t\t\t\t YOUR SCORE IS NOT SUFFICIENT TO JOIN THIS COLLEGE ")
        print(" \t\t\t\t\t\t BETTER LUCK NEXT TIME ")
    else:
        print("\t\t\t\t\t\t YOU ARE SELECTED TO JOIN IN THIS COLLEGE ")
        print("\t\t\t\t\t\tPLEASE CHECK YOUR DETAILS ")
        print(" student's name is :",name)
        print(" student's gender is :",gender)
        print(" DOB of the student is :",DOB)
        print(" student's address is :",address)
        print(" your village pincode is :",pincode)
        print(" your guardian's name is :",guardian_name)
        print(" your mobile number is :",number)
        s1=" name :"+ name
        s2=" gender :"+ gender
        s3=" DOB :"+ DOB
        s4=" address :"+ address
        s5=" pincode :"+ pincode
        s6=" guardian name :" + guardian_name
        s7=" number :"+ number
            
        print("press yes if all the details are correct ")
        p=time.asctime()
        details_correct=input()
        if(details_correct=='YES' or details_correct=='yes'):
            print("\t\t\t\t\t\t YES !! YOU MADE IT ")
            print(" your date of joining is :",p)
            s8=" date of joining :"+ p
            
            with open("details.txt","a") as f:
                f.write(s1+'\n')
            with open("details.txt","a") as f:
                f.write(s2+'\n')
            with open("details.txt","a") as f:
                f.write(s3+'\n')
            with open("details.txt","a") as f:
                f.write(s4+'\n')
            with open("details.txt","a") as f:
                f.write(s5+'\n')
            with open("details.txt","a") as f:
                f.write(s6+'\n')
            with open("details.txt","a") as f:
                f.write(s7+'\n')
            with open("details.txt","a") as f:
                f.write(s8+'\n')
            

            with open("joined.txt","a") as file:
                file.write(s1+'\n')

            file = open("joined.txt","r")
            line_count = 0
            Content = file.read()
            CoList = Content.split("\n")
            for i in CoList:
                if i:
                    line_count +=1
            print(" your admission number is :",line_count)
            s9=" admission number :"+str(line_count)
            with open("details.txt","a") as f:
                f.write(s9+'\n')
                
            print(" YOU HAVE TO PAY 100000 RUPEES")
            payfee=input(" DO YOU WANT PAY THE FEE NOW (yes/no): ")
            if(payfee=="yes" or payfee=="YES"):
                print("\t\t\t\t YES .... YOU HAVE DONE IT ")
                with open("feepaid.txt","a") as f:
                    f.write(s1+'\n')
            
                print("please collect the receipt")
                print("---------------------------------------------------------------------------------------------------------------------------------")
                print("| Name         :",name,"                              guardian name   :",guardian_name,"                                         ")
                print("| Gender       :", gender,"                           Date of Birth   :",DOB,"                                                   ")
                print("| address      :",address,"                           pincode         :",pincode,"                                               ")
                print("| phone number :",number,"                            Date of Joining :",p,"                                                     ")
                print("| your admission number is :",line_count,"                            fee paid        :100000                                                    ")
                print("---------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("please pay before one month of commencement of exams")
        else:
            print("OK THEN !!! ENTER YOUR DETAILS AGAIN ")
            
def checking():
    print("\t\t\t\t\t\t WELCOME TO CHECKING SECTION ")
    check=int(input("enter the student admission number to check :"))
    file = open("joined.txt","r")
    line_count = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            line_count +=1

    file=open("details.txt")
    lines_to_print=[9*(check-1),9*(check-1)+1,9*(check-1)+2,9*(check-1)+3,9*(check-1)+4,9*(check-1)+5,9*(check-1)+6,9*(check-1)+7,9*(check-1)+8]
    for index,line in enumerate(file):
        if ( index in lines_to_print):
            print(line,end=" ")
    file.close()

    
def joined():
    print("THE NAMES OF STUDENTS JOINED ARE :")
    with open("joined.txt","r") as file:
            print(file.read())
            
def remaining():
    file = open("joined.txt","r")
    line_count = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            line_count +=1
    print(" THE TOTAL ADMISSIONS REMAINING IS :",1000-line_count)


def feepaid():
    with open("feepaid.txt") as f:
        print(f.read())

print("\t\t\t\t\t\t WELCOME TO THE COLLEGE OF ENGINEERING ")
print("1. TAKING ADMISSION")
print("2. CHECKING FOR STUDENT DETAILS")
print("3. NAMES OF THE STUDENTS JOINED IN THE COLLEGE")
print("4. REMAINING SEATS LEFT IN THE COLLEGE")
print("5. STUDENTS WHO PAID FEE")
n=input("\t\t\t\t\t\t ENTER THE ACTION YOU WANT TO PERFORM ")
if(n=='1'):
    admission()
elif(n=='2'):
    checking()
elif(n=='3'):
    joined()
elif(n=='4'):
    remaining()
elif(n=='5'):
    feepaid()
else:
    print("\t\t\t\t\t\t ENTER THE  CORRECT ACTION ")
   
