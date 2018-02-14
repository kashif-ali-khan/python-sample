def sum(arg1,arg2=10,arg3=[5,7]):
	total = arg1 + arg2 + arg3;
	return total , "Hello i am done";
	
total,msg = sum(10,20,30);

print(total);
print(msg);	

