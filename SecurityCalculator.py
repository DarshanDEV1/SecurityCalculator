password="HELLO_OPEN_WORLD@123"
enter = " "
while password != enter :
	enter=input("Enter PASSWORD::- ")
if enter != password:
	print("WRONG PASSWORD ENTER AGAIN")
	enter=input("Enter PASSWORD::- ")
else:
	print("WELCOME TO THE PYTHON CALCULATOR:::-- ")
	number1=float(input("enter your first number: "))
	op=input("enter the operator sign: ")
	number2=float(input("enter your second number: "))
if  op=="+":
	print(number1 + number2)
elif op=="-":
	print(number1 - number2)
elif op=="*":
	print(number1 * number2)
elif op=="/":
	print(number1 / number2)
else:
	print("Invalid entry...")
print("CALCUALTION DONE SUCESSFULLY")