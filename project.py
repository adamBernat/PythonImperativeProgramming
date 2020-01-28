import random
 
 
def help1():
    print("choose program function\n")
    print(" 1. Calculator (type '1')")
    print(" 2. String spaces remover(type '2')")
    print(" 3. Lambda Function Calculator (type '3')")
    print(" 4. Collatz Conjecture Simulation (type '4')")
    print(" 5. Gapful number checker (type '5')")
    print(" y. To end program type 'q'")
    print(" z. To acces help type 'h'")
 
#function definitions
#1. calculator
def Calc():
    quit = False
    quit2 = False
    dzialanie =' '
    while quit !=True:
        x=0.0
        y=0.0
        z=0.0
        print("Welcome in calculator")
   
        while quit2 != True:
            print("\nto add two numbers type '+'")
            print("to subtract two numbers type '-'")
            print("to multiply two numbers type'*'")
            print("to divide two numbers type '/'")
            print("to floor divide two numbers type '//'")
            print("to exit type 'q'")
            dzialanie=(input('\n which operation you want to choose? '))
           
           
            if str(dzialanie)=='+':
                x =input('wpisz pierwsza liczbe: ')
                y =input('wpisz druga liczbe: ')
                try:
                    z =float(x)+float(y)
                    print ("result is: " + str(z))
                except (TypeError, ValueError):
                    print("input only digits!!")
               
   
            if str(dzialanie)=='*':
                x =input('wpisz pierwsza liczbe: ')
                y =input('wpisz druga liczbe: ')
                try:
                    z =float(x)*float(y)
                    print ("result is: " + str(z))
                except (TypeError, ValueError):
                    print("input only digits!!")
               
   
            if str(dzialanie)=='-':
                x =input('wpisz pierwsza liczbe: ')
                y =input('wpisz druga liczbe: ')
                try:
                    z =float(x)-float(y)
                    print ("result is: " + str(z))
                except (TypeError, ValueError):
                    print("input only digits!!")
   
            if str(dzialanie)=='/':
                x =input("enter number to be divided: ")
                y =input("enter divisor: ")
                try:
                    z =float(x)/float(y)
                    print ("result is: " + str(z))
                except (TypeError, ValueError, ZeroDivisionError):
                    print("input only digits and don\'t divide by zero")
           
            if str(dzialanie)=="//":
                x=input("enter number to be floor divided: ")
                y=input("enter divisor of a floor division: ")
                try:
                    z =float(x)//float(y)
                    print ("result is: " + str(z))
                except (TypeError, ValueError, ZeroDivisionError):
                    print("input only digits and don\'t divide by zero")               
               
               
            if str(dzialanie)=='q':
                quit = True
                quit2 = True
                print ("\nsubprogram finished, returning to main menu\n")
                break
            else:
                x=1
 
#2. spaces remover
def SpcRmv():
    string = input("enter your string here: ")
    print("string to be modified: \n" + string)
    string = string.replace(" ","")
    print("string after operation:\n" + string)
   
    if (" " in string) == False:
        print("spaces were removed")
    else:
        print("An error occured")
    print ("\nsubprogram finished, returning to main menu\n")
   
#lambda calculator
def LambdaCalculator():
    quit_l = False
    quit2_l = False
    dzialanie =' '
    while quit_l !=True:
        x=0.0
        y=0.0
        z=0.0
        print("Welcome in calculator")
   
        while quit2_l != True:
            print("\nto add two numbers type '+'")
            print("to subtract two numbers type '-'")
            print("to multiply two numbers type'*'")
            print("to divide two numbers type '/'")
            print("to exit type 'q'")
            dzialanie=(input('\n which operation you want to choose? '))
           
            #excpetion handler and adding        
            def executeAddition(x, y):
                try:
                    z = lambda x, y: int(x) + int(y)
                    # you need to execute the lambda, like this:
                    return z(x, y)
                except:
                    print('Exception caught')
       
            if str(dzialanie)=='+':
                print("result is: "  + str(executeAddition(input("input 1st number: "), input("input 2nd number: "))))
   
            
            #excpetion handler and multiplying        
            def executeMultip(x, y):
                try:
                    z = lambda x, y: int(x) * int(y)
                    # you need to execute the lambda, like this:
                    return z(x, y)
                except:
                    print('Exception caught')

            if str(dzialanie)=='*':
                multip = lambda x,y : x * y
                print("result is: "  + str(executeMultip(input("input 1st number: ")), int(input("input 2nd number: "))))
       
            #excpetion handler and subtracting        
            def executeSubtract(x, y):
                try:
                    z = lambda x, y: float(x) - float(y)
                    # you need to execute the lambda, like this:
                    return z(x, y)
                except:
                    print('Exception caught')
                
            if str(dzialanie)=='-':
                subtract = lambda x,y : x - y
                print("result is: "  + str(executeSubtract(input("input 1st number: ") , input("input 2nd number: "))))
  
                
            #excpetion handler and dividing        
            def executeDiv(x, y):
                try:
                    z = lambda x, y: float(x) / float(y)
                    # you need to execute the lambda, like this:
                    return z(x, y)
                except:
                    print('Exception caught')

            if str(dzialanie)=='/':
                print("result is: "  + str(executeDiv(input("input 1st number: "), input("input 2nd number: "))))

   
                   
   
            if str(dzialanie)=='q':
                quit_l = True
                quit2_l = True
                print ("\nsubprogram finished, returning to main menu\n")
                break
            else:
                x=1
 
 
#collatz conjecture simulation
def CollatzConjectureSimulation(): 
    ColRand=0
    RngVal=0
   
    print("Welcome in Collatz!")
   
    #Collecting range of random number to be found
    while RngVal == 0:
        try:
            RngVal = int(input("input range of random number (from 5 to x) x = "))
            if RngVal ==0:
                raise ValueError
        except (TypeError, ValueError):
            print ("input only integers and not zero")
           
           
           
    #random number generation    
    ColRand = random.randint(5,int(RngVal))
   
    #feedback
    print("your range of random number to be choosen is from 5 to " + str(RngVal))
    print("your random number is: " + str(ColRand))
   
    #processing and printing
    End = 0
    while End != 1:
        if (ColRand %2 ==0 and ColRand != (0 and 1)):
            ColRand = ColRand/2
            print("number was even, divising by 2    = " + str(int(ColRand)))
        if (ColRand %2 !=0 and ColRand !=1):
            ColRand = ColRand*3 +1
            print("odd number, tripling and adding 1 = " + str(int(ColRand)))
        elif ColRand == 1:
            print("you reached 4-2-1 sequence, finishing program")
            End = 1
 
#gapful number seeker
def Gapful():
    collected = False
    while collected == False:
        divisor=""
        try:
            #collecting number and turning input string to an integer
            rawNumber=input("Enter a number to check if its gapful (or type \"q\" to quit): ")
            if rawNumber == "q":
                collected= True
                break
            number=int(rawNumber)
           
            #creating divisor taken from first and last digit of number
            numberLen=len(rawNumber)
            divisor=int((rawNumber[0])+(rawNumber[numberLen - 1]))
            collected = True
           
        except (TypeError, ValueError):
            print("enter integers only!")
            collected = False
       
           
        #number analysis and feedback  
        if collected == True:
            print("Your number was: " + rawNumber)
            print("Its divisor is: " + str(divisor))
            if number % divisor == 0:
                print(rawNumber + " modulo " + str(divisor) + " is zero so your number is gapful")
                collected = False
            if number % divisor !=0:
                print("your number is not gapful")
                collected = False
 
 
#program
Quit=""
help1()
while Quit != True:
    MainMenu = input("input:")
   
    if MainMenu == "1":
        Calc()
        MainMenu =""
       
    if MainMenu=="2":
        SpcRmv()
        MainMenu =""
   
    if MainMenu=="3":
        LambdaCalculator()
        MainMenu=""
   
    if MainMenu=="4":
        CollatzConjectureSimulation()
        MainMenu=""
       
    if MainMenu=="5":
        Gapful()
        MainMenu=""
       
    if MainMenu=="q":
        Quit=True
       
    if MainMenu=="h":
        help1()
       
    elif MainMenu != "":
        print("error")