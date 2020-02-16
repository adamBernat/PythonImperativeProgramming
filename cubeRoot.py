#required
import math


def cubeRoot():
	x = input('input number to be cube root found: ')

	#creating divisor for cube root base seek
	divisor = "0."
	for i in range (len(x)-2):
		divisor = divisor + "0"
	divisor = divisor + "1"
	#print(str(divisor))


	# OLD creating addition step for calculation of root OLD!!!!
	#divisor2 = "0.00"
	#for i in range (len(x)-2):
	#	divisor2 = divisor2 + "0"
	#divisor2 = divisor2 + "1"


	#creating addition step for calculation of root
	if len(x) <= 3:
		divisor2 = "0.0000001"
	
	if (len(x) <= 5) and (len(x) > 3):
		divisor2 = "0.000001"

	if (len(x) <= 6) and (len(x) > 5):
		divisor2 = "0.00001"

	if (len(x) <= 8) and (len(x) > 6):
		divisor2 = "0.0001"

	if (len(x) <= 10) and (len(x) > 8):
		divisor2 = "0.0001"

	if len(x) > 10:
		divisor2 = "0.0001"

	#creating smallest number to be compared to cube root candidate
	seeked = float(x) * float(divisor)

	#Declaring variable which holds calculated cube root until it reach (by power of three) input number
	seeked3 = 1 


	#if len(x) <= 10:
	while  (seeked3 + float(divisor2)) < int(x):
		seeked = seeked + float(divisor2)
		seeked3= seeked ** 3

	#if len(x) > 10:
	#	while  (seeked3 + float(divisor2)) < int(x):
	#		seeked = seeked + float(divisor2)
	#		seeked3= seeked ** 3


	# result printing
	print("calculated cube root is: " + str(seeked))
	print("cube root to ^3 is: " + str(seeked3) + "\n")

	# comparision to math.pow method
	mathpowresult = math.pow(int(x),1/3)
	mathpowresultCubed = mathpowresult ** 3
	print("calculated math pow result is: " + str(mathpowresult))
	print("math.pow cube root to ^3 is: " + str(mathpowresultCubed))