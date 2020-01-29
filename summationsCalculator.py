#Summations Calculator

#Create a program that takes 3 inputs, a lower bound, an upper bound and the expression. Calculate the sum of that range based on the given expression and output the result.

#For Example:
#Input: 2 4 *2
#Output: 18 (2*2 + 3*2 + 4*2)

#Input: 1 5 %2
#Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)

def summCalc (lower, higher, expression):
    calcLine = "" # storage of final expression

    for num in range (int(lower),int(higher)):
        calcLine += "{}{} + ".format(str(num), expression)

    calcLine += "{}{} + ".format(higher, expression)

    print(eval(calcLine),"({})".format(calcLine)) # evaluate the resulting line

summCalc(*input().split(" "))