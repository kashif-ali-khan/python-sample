class justcounter:
	__secretcount=0;
	def __init__(self,count):
		self.count = count;
		
	def countVal(self):
		self.count+=1;
		print("count is %d"%self.count);
		

count = justcounter(1);		
count.countVal();

count.countVal();
count.countVal();
count.countVal();