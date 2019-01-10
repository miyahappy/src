# -*- coding: utf-8 -*-
import os,sh
os.chdir('/home/userroot/ncbi/public/sra/')
listSra =  open('./SRR_Acc_List.txt')
all_lines = listSra.readlines()
for line in all_lines:
    print (line)
    os.system('prefetch %s' %(line))
    os.system('fastq-dump %s' %(line))
listSra.close()
