'''
Shawn Arreguin
8/25/25
Builds a fasta file for each chloroplast or mito gene. The fasta file contains all the sequences from each species
that correspond to a given gene. The input file is a fasta file with all sequences in it. You must specify the minimum number of taxa as the second argument

python3 geneFasta.py <large_fasta.fa> <minimum_number_of_taxa> <outDir>

Updated: 2/11/26
'''

import sys

allFasta=open(sys.argv[1],"r")
taxaNum=int(sys.argv[2])
outDir=sys.argv[3]

def BuildGeneDict(file):
    '''This function calls on a fasta file. It builds two dictionaries one of each header/sequence pair and another with the key as the gene name and the gene file name, number of sequences of the gene, and sequence names as the value in a list format'''
    GeneDict={}
    GeneFilesDict={}
    for line in file:
        if ">" in line: #good way to do it imo bcuz the first character of a gene name in a fasta should be ">" (only have to check the first one)
            line=line.strip('\n')
            line=line.strip(" ")
            name=line[1:]
            a=line
            GeneDict[a]="" #the header becomes the key
            name=name.split("-")
            gene=name[1]
            if gene in GeneFilesDict:
                GeneFilesDict[gene][1]+=1
                GeneFilesDict[gene].append(line)
            else:
                geneFile=gene+".fa"
                GeneFilesDict[gene]=[geneFile,1,line]
        else:
            GeneDict[a]+=line #add the seq line to the value until we get to the next header line or the file ends
    return GeneDict, GeneFilesDict

def FileWriter(fasta,taxaNum):
    Genes, GeneFiles = BuildGeneDict(fasta)

    for x in GeneFiles:
        if GeneFiles[x][1] >= taxaNum:
            for i in GeneFiles[x][2:]:
                tmp=outDir+"/"+GeneFiles[x][0]
                with open(tmp,"a") as file:
                    file.write(i.split("-")[0]+'\n'+Genes[i])
        else:
            print(x,GeneFiles[x][1])

FileWriter(allFasta,taxaNum)

