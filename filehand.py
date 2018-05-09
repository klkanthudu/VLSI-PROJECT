#!/usr/bin/python3

#how to write in file filehandling

with open("outfile", "w") as fobj:
	fobj.write("my name is lakshmikanth \n");
	fobj.writelines("i am coming from atp\n" + "atp is dict in ap\n");
	lines="hi lakshmikanth\n";
	lines=lines + "hi vicky\n";
	fobj.writelines(lines);
	fobj.close();


#count the lines in a file 
print(".................................\n");


count_lines=0;
l1=[];
with open("outfile", "r") as fobj:
	for line in fobj:
		line=line.strip();
		count_lines += 1;
		l1.extend(line.split(" "));
		print(line);
print("number of lines in the file:", count_lines);

#count the no.of words in a file.
 
print("...................................\n")
 
count1=0;
for ele in l1:
	count1=count1+1;
print("number of words in file:", count1);

#count the no.of repeated words in a file.
print(".................................\n")

dict={};
for w in l1:
	if w in dict.keys():
		dict[w]+=1;
	else:
		dict[w]=1;
print("no of repeated words in file:", dict);

