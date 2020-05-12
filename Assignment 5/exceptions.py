# IO Error
try:
	fh = open("testfile", "r")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print("Error: can\'t find file or read data")
else:
	print("Written content in the file successfully")

# Index Error
newlist = ["PPL", "Assignments", "Project"]
try:  
	print("List is:", newlist)
	for i in range(4):
		print(newlist[i])
except IndexError: 
	print("An index error occurred")
	
	
# Zero division error
def division(x, y):
	try:
		result = x/y
		print("Result is: ", result)
	except ZeroDivisionError:
		print("division by zero not allowed")


division(2, 0)
