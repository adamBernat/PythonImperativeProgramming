x = input('input number to be cube root found: ')

#creating divisor for cube root base seek
divisor = "0."
for i in range (len(x)-2):
	divisor = divisor + "0"
divisor = divisor + "1"


# OLD creating addition step for calculation of root OLD!!!!
#divisor2 = "0.00"
#for i in range (len(x)-2):
#	divisor2 = divisor2 + "0"
#divisor2 = divisor2 + "1"


#creating addition step for calculation of root
if len(x) <= 3:
	divisor2 = "0.000000001"
	
if (len(x) <= 5) and (len(x) > 3):
	divisor2 = "0.000001"

if (len(x) <= 6) and (len(x) > 5):
	divisor2 = "0.00001"

if (len(x) <= 7) and (len(x) > 6):
	divisor2 = "0.0001"

if len(x) > 7:
	divisor2 = "0.0001"

#creating smallest number to be compared to cube root candidate
seeked = float(x) * float(divisor)

#Declaring variable which holds calculated cube root until it reach (by power of three) input number
seeked3 = 1 
x = int(x)


while  seeked3 < x:
	seeked = seeked + float(divisor2)
	seeked3= seeked * seeked
	seeked3= seeked3 * seeked



print("calculated cube root is: " + str(seeked))
print("cube root to ^3 is: " + str(seeked3))