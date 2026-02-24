'''
Shawn Arreguin
2/23/26

This script removes hypotheical genes from the genome. Essentially, unknown genes that have been added to the genome will be removed. 
I only want known genes.
'''


import sys

genome=open(sys.argv[1],"r")
tmp=sys.argv[1].split(".")
out=tmp[0]+"_RM."+tmp[1]
print("Output written to:",out)

p=True
c=0
for line in genome:
	if line[0]==">" and "[gene=" in line:
		#print(line)
		with open(out,"a") as outfile:
			outfile.write(line)
		p=True
	elif line[0]==">" and "[gene=" not in line:
		c+=1
		p=False
	elif p==True and line[0]!=">":
		#print(line)
		with open(out,"a") as outfile:
			outfile.write(line)
	elif p==False and line[0]!=">":
		pass

print("Bad seq count:",c)
