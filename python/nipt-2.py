# coding=utf-8
import os,datetime,shutil,subprocess,time,psutil
import multiprocessing 
import threading
from threading import Thread
import numpy as np
os.chdir('/home/userroot/nipt')

file_dir = input("Enter your fastq folder name:")
fq_name = os.listdir('./fq/'+file_dir)
i = datetime.datetime.now()
#print(fq_name)
filename_fq=open('./filename/'+str(i.year)+str(i.month)+str(i.day)+'.txt',"w")
filename_fq.writelines([line+'\n' for line in fq_name])
n = len(fq_name)
m = n

#os.system("bedtools makewindows -g ./bed/chr_size/chr_size.sizes -w 300000 > ./bed/bin_ucsc_hg19.bed")
#os.system("bedtools nuc -fi ./fa/fasta/ucsc.hg19.fasta -bed ./bed/bin_ucsc_hg19.bed | cut -f 1-3,5 > ./gc_bed/gc_bin.bed")

#class nipt(object):
#def __init__(self,fq, verbose=False):
#  self.fq = os.path.abspath(fq)
def setdir(fq):
  input_file= './fq/'+file_dir+'/'+fq
  bam_file= './bam/'+fq+'.bam'
  sort_bam_file='./sort_bam/sort_'+fq+'.bam'
  sort_bam_file_1='./sort_bam/sort_'+fq+'.bam'
  rmdup_sort_bam_file= './rmdup_sort_bam/rmdup_sort_'+fq+'.bam'
  counts_file='./counts/'+fq+'.counts' 
  a = [input_file,bam_file,sort_bam_file,sort_bam_file_1,rmdup_sort_bam_file,counts_file]
  return a
def mapping(fq,zuse = 0):
	a = setdir(fq)
	p1 = subprocess.Popen(["subread-align -t 1 -T 40 -M 0 -I 0 -i ./fa/ucsc_hg19/ucsc_hg19 -r"+a[0]+" -o"+a[1]+" > "+"./log/lod.txt"],shell=True) #mapping
	if zuse == 1:
		p1.wait()
	return 
	
	
def sorting(fq):
  a = setdir(fq)
  subprocess.Popen("rm ./bam/*.indel",shell=True) 
  p2 = subprocess.Popen(["samtools sort -@ 40 -o "+a[2]+" "+a[1]],shell=True) #sort
  #p2.wait()
  return  
  
  
def rmdup(fq):
  a = setdir(fq)
  p3 = subprocess.Popen(["samtools rmdup -s "+a[3]+" "+a[4]],shell=True) #remove duplications
  #p3.wait()
  return 
  
  
def count(fq):
  a = setdir(fq)
  p4 = subprocess.Popen("bedtools coverage  -abam ./bed/bin_ucsc_hg19.bed -b "+a[4]+" > "+a[5],shell=True) 
  #p4.wait()
  return   
  

def align(fq,zuse = 0):
	cpu = psutil.cpu_percent(interval=1)
	if float(cpu) < 75.0:
		setdir(fq)
		mapping(fq,zuse)
		time.sleep(8)
	else:
		time.sleep(5)
		cpu = psutil.cpu_percent(interval=1) 
		while float(cpu) > 75.0:
			time.sleep(8)
			cpu = psutil.cpu_percent(interval=1) 
		else:
			setdir(fq)
			mapping(fq,zuse)
			time.sleep(8)
			
			
def sort(fq):
	cpu = psutil.cpu_percent(interval=1)
	if float(cpu) < 80.0:
		sorting(fq)
		time.sleep(1)
	else:
		time.sleep(1)
		cpu = psutil.cpu_percent(interval=1) 
		while float(cpu) > 80.0:
			time.sleep(1)
			cpu = psutil.cpu_percent(interval=1) 
		else:
			sorting(fq)
			time.sleep(1)
	return
	

n = 96				 
def main():
	print(n)
  #b = np.arange(0,n-1,2)  
	#for i in range(n-1):
	#	align(fq_name[i])
	#time.sleep(300)
	#for i in range(n-1):	
	#	time.sleep(4)	
	#	sort(fq_name[i])
	#time.sleep(30)
	for i in range(n-1):	
		time.sleep(15)	
		rmdup(fq_name[i])
	time.sleep(220)
	for i in range(n-1):	
		time.sleep(20)
		count(fq_name[i])
	return


if __name__ == '__main__':
 main() 
 #for line in fq_name: 
  #t1 = threading.Thread(mapping(line))
  #threads.append(t1)
  #for t in threads:
  #  t.setDaemon(True)
  #  t.start()	
  #p = multiprocessing.Pool(processes=40)
  #for i in range(10):
  #  p.apply_async(main) 
    
    #p1 = multiprocessing.Process(mapping(line))
    #p1.start()  
    #p.apply_async(mapping(line))
  #print("#######unanalysed/total:"+str(n-1)+"/"+str(m)+";Progress status:"+str(format(1-((n-1)/m),'.0%'))+"########") #this is a counter.
  #n = n-1
 # p.close() # 开始执行进程
 # p.join() # 等待子进程结束
filename_fq.close()



