import MySQLdb
try:
	db = MySQLdb.connect("localhost","root","root","kashif");
	print(db)
	'db.query("select * from movies");'
	'r=db.store_result();'
	'result = r.fetch_rows();'
	'print(result);'

c=db.cursor();
c.execute("select * from movies");
result = c.fetchall();
#print(result);
for data in result:
	print(data[0])

