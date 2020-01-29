##### Code made by Nevfy: 2018-04-19 #####
 
# Challenge: Summations Calculator
# Solution: Optimal
 
 
'''
 
Summations Calculator
 
Create a program that takes 3 inputs, a lower bound, ang upper bound and the expression. Calculate the sum of that range based on the given expression and output the result.
 
For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)
 
Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)
   
'''
 
 
def sum_calc(lowerBound,higherBound,expression):
 
    calcLine = "" # storage of final expression
   
    # for all num in range (unless the last) add number, expression and sign '+' to the line
    for num in range(int(lowerBound),int(higherBound)):
        calcLine += "{}{} + ".format(str(num),expression)
   
    # add last number with expression    
    calcLine += "{}{}".format(higherBound,expression)
   
    print(eval(calcLine),"({})".format(calcLine)) # evaluate the resulting line
 
   
 
## main block    
sum_calc(*input().split(" "))
 
 
 
## test block
#sum_calc('2','4','*2')