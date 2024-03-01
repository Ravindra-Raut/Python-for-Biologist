#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:28:29 2024

@author: ravindraraut
"""

#%%


#%%

#file handeling

# r- read # a- append- write and edit

input_file=open("/Users/ravindraraut/Desktop/learn_biopython/sequence.fasta", "r")
output_file=open("/Users/ravindraraut/Desktop/learn_biopython/sequence2.fasta", "a")

count=0

seq=""

output_file.write("Composition of DNA" + "\n")

for line in input_file:
    line = line.rstrip("\n")
    count=count+1
    
    if count==1:
        output_file.write(line + "\n")
        
    else:
        seq=seq+line
        
print(seq)

length1=len(seq)
output_file.write("\n" + "length of the seq is:" +str(length1) + "\n")

nuc=("A", "T", "G", "C", "N")
gc=0


for x in nuc:
    n_count=seq.count(x)
    output_file.write(str(x)+ "\t" +str(n_count) + "\n")
    if x=="G" or x=="C":
        gc=gc+n_count
    print(x, n_count)
    
percent_gc=(gc/length1)*100
output_file.write("\n"+ "GC content=" + str(percent_gc) + "\n")

input_file.close()
output_file.close()



#%%
import glob

filenames=glob.glob("/Users/ravindraraut/Desktop/learn_biopython/*.fasta")
print(filenames)

#%%
nuc=("A","T","G","C","N")
file22=open("/Users/ravindraraut/Desktop/learn_biopython/results.txt", "a")

#%%
for i in filenames:
    count=0; seq="";gc=0;percent_gc=0
    
    file1=open(i, "r")
    
    for line in file1:
        line=line.rstrip("\n")
        count=count+1 
        
        if count==1:
            file22.write(line + "\n")
        else:
            seq=seq+line
            
    length1=len(seq)
    for x in nuc:
        n_count=seq.count(x)
        file22.write(str(x)+str(n_count)+ "\t")
        if x=="G" or x=="C":
            gc=gc+n_count
            
    percent_gc=(gc/length1)*100
    file22.write("\n"+"GC content="+ str(percent_gc)+ "\n")
    file1.close()
    
file22.close()

#%%        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

