# "r"  - Read

# "a"  - Append

# "w"  - Write

# "x"  - Create

# "t"  - Text

# "b"  -Binary

#open & Read File

# f = open('test.txt', 'r')  # R - Read

# print(f.name)

# f.close()



# with open('test1.txt', 'a') as g:

# 	g.write('This is line number 6'+"\n")

# 	print(g,end='')


# with open('test.txt', 'r') as f:

# 	f_text = f.readline()
# 	print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for line in f:
	# 	print(line,end='')

	# f_text = f.read(500)
	# print(f_text,end='')

	# size_to_read = 10
	# f_text = f.read(size_to_read)

	# while len(f_text) > 0:
	# 	print(f_text,end='')



	f_text = f.read(100)

	while 100 > 0:
		print(f_text,end='')