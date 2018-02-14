try:
	fh = open('testfile','w');
	fh.write("This is test file for exception handling")
except IOerror:
	print("Error");
else:
	print("No error")
	
def temp_convert(var):
	try:
		return int(var);
	except TypeError:
		print("This argument this not contain numbers"+Argument);
		
		
temp_convert('This')		