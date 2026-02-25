'''
Shawn Arreguin
3/10/25
Given the duplicated genes in a chloroplast genome, this small script will pull only one of the two duplicates, creating a fasta with one sequence per gene. 

Update: 2/11/26
This will now pull the longest gene of the two.
'''

import sys

file = open(sys.argv[1],"r")
newfile = open(sys.argv[2],"w")

geneDict={}
repeatDict={}
repeats=[]

a=True
for line in file:
    '''If its the header sequence and has not beeen inserted into the geneDict, write it to a file and set a to true. 
    If its already been written to geneDict, set a to false. Only write the sequence to the dictionary when a is true, prevents 
    adding the duplicated sequence.'''
    line=line.strip()
    if ">" in line and line not in geneDict:
        header=line
        geneDict[header]=""
        #newfile.write(header+"\n")
        a=True
    elif ">" in line and line in geneDict:
        header2=line
        repeatDict[header2]=""
        repeats.append(header2)
        #newfile.write(header+"\n")
        a=False
    elif ">" not in line and a == True:
        seq=line+"\n"
        geneDict[header]+=seq
        #newfile.write(seq)
    elif ">" not in line and a ==False and len(line) >=1:
        #print(line)
        seq2=line+"\n"
       # print(seq)
        repeatDict[header2]+=seq2
        #print(repeatDict[header])
    else:
        print(line)

for x in repeats:
    #print(repeatDict[x], geneDict[x])
    #print(x, len(repeatDict[x]), len(geneDict[x]))
    if len(repeatDict[x]) > len(geneDict[x]):
        print("greater", x, len(repeatDict[x]), len(geneDict[x]))
        geneDict[x]=repeatDict[x]
        print("greater", x, len(repeatDict[x]), len(geneDict[x]))
    elif len(repeatDict[x]) < len(geneDict[x]):
        print("less", x, len(repeatDict[x]), len(geneDict[x]))
    else:
        print(x, len(repeatDict[x]), len(geneDict[x]))


for key in geneDict:
    newfile.write(key)
    newfile.write('\n')
    newfile.write(geneDict[key])



newfile.close()
file.close()

