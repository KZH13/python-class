#Boolean Expression


# print(20 > 10)
# print(20 == 10)
# print(20 < 10)
# print(bool("Hello World"))
# print(bool(20))



# Python Conditions 

# Equals              ->  x  == y
# Not Equals          ->  x  != y
# Less than           ->  x  <  y
# Less than or equal to ->  x  <=y
# Greater than        ->  x  >  y
# Greater than or equal to ->  x >=y


# Boolean Or          ->  x or y, x | y
# Boolean AND         ->  x and y , x & y
# Boolean NOT         ->  not x

# #If  statement

# x = 70
# y = 60

# if x > y:
# 	print("x is greater than y")
# elif x == y:
# 	print("x and y are equal")


# #Else

# x = 50
# y = 150
# if x > y:
# 	print("x is greater than y")
# elif x == y:
# 	print("x and y are equal")
# else:
# 	print("x is less than y")


# #Short Hand If

# if x > y: print("x is greater than y")


# #Short Hand IF....Else

# x = 50
# y = 150
# print(x) if x>y else print(y)



# #And is logical operator 


# x = 50
# y = 40
# z = 100
# if x>y and z > x:
# 	print("All conditions are true")


# #OR is logical operator 

x = 50
y = 40
z = 100
if x > y or z > y:
	print("one of the condition is true")
elif x > y and z >y :
	print("All condition are true")
else:
	print("nothing else")


# 	#Nested IF is if statement in if statements

# 	x = 50

# 	if x > 10:
# 		print("x is ten")
# 	    if x > 20:
# 		print("x is greater than 20")
# 	else: 
# 		print("No,x is not greater than 20")



# 	#Pass Statement

# 	x = 100
# 	y = 50
# 	if x > y:
# 		pass



# 	-------------------


# 	x = int(input("Please enter an interger:"))

# 	if x < 0:
# 		x = 0
# 		print('Negative changed to zero')
# 	elif x == 0:
# 		print('Zero')
# 	elif x == 1:
# 		print('Single')
# 	else:
# 		print('More')