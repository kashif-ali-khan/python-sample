fo = open('foo.txt','a');
str = fo.read();

print("this content of file is  "+str);

fo.write("This is hello");

print("this content of file is  "+str);
fo.close()