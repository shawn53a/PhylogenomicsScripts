'''
Shawn Arreguin
2/24/26

This script removes a gene or list of genes that I give it. Genes are separated by "-"

python3 removeGene.py <fasta file> <list-of-genes>
'''


import sys

genome=open(sys.argv[1],"r")
genes=sys.argv[2]
print("Genes to be removed:",genes)

tmp=sys.argv[1].split(".")
out=tmp[0]+"_RM."+tmp[1]
print("Output written to:",out)

p=True
c=0
b=0
for line in genome:
	if line[0]==">":
		tmp=line.strip().split("-")
		if tmp[1] in genes:
			print(tmp[1])
			p=False
			c+=1
		else:
			#print("good",line)
			with open(out,"a") as outfile:
		 		outfile.write(line)
			p=True
	elif p==True and line[0]!=">":
	 	#print(line)
	 	with open(out,"a") as outfile:
	 		outfile.write(line)
	elif p==False and line[0]!=">":
	 	b+=1

print("Seqs Removed:",c,b)
