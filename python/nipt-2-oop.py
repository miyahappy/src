# coding=utf-8
import os,datetime,shutil,subprocess,time,psutil
import multiprocessing 
#import threading
#from threading import Thread

os.chdir('/home/userroot/data/nipt')
file_dir = input("Enter your fastq folder name:") #FQ files folder
fq_name = os.listdir('./fq/'+file_dir)
i = datetime.datetime.now()
start_time = str(i)[0:19]
#print(fq_name)
filename_fq=open('./filename/'+str(i.year)+'-'+str(i.month)+'-'+str(i.day)+'-'+str(i.hour)+'：'+str(i.minute)+'.txt',"w")
log=open('./log/'+str(i.year)+'-'+str(i.month)+'-'+str(i.day)+'-'+str(i.hour)+'：'+str(i.minute)+'.txt',"a")
filename_fq.writelines([line+'\r\n' for line in fq_name])
n = len(fq_name)
m = n

#######>> making bin file and gc_bin file <<########
#os.system("bedtools makewindows -g ./bed/chr_size/chr_size.sizes -w 300000 > ./bed/bin_ucsc_hg19.bed")
#os.system("bedtools nuc -fi ./fa/fasta/ucsc.hg19.fasta -bed ./bed/bin_ucsc_hg19.bed | cut -f 1-3,5 > ./gc_bed/gc_bin.bed")

class nipt(object):
	'''parameter_1: fq files'''
	'''parameter_2: direction of fq files(keyboard input)'''
	'''cpu rate cutoff and wait time is set for 96 or more samples.DON'T CHANGE!'''
	def __init__(self,fq,file_dir):
		self.fq = fq
		self.file_dir = file_dir

	def setdir(self):
		input_file= './fq/'+self.file_dir+'/'+self.fq
		bam_file= './bam/'+self.fq+'.bam'
		sort_bam_file='./sort_bam/sort_'+self.fq+'.bam'
		sort_bam_file_1='./sort_bam/sort_'+self.fq+'.bam'
		rmdup_sort_bam_file= './rmdup_sort_bam/rmdup_sort_'+self.fq+'.bam'
		counts_file='./counts/'+self.fq+'.counts' 
		a = [input_file,bam_file,sort_bam_file,sort_bam_file_1,rmdup_sort_bam_file,counts_file]
		return a
		
	def mapping(self,zuse = 0):
		a = self.setdir()
		p = subprocess.Popen(["subread-align -t 1 -T 40 -M 0 -I 0 -i ./fa/ucsc_hg19/ucsc_hg19 -r"+a[0]+" -o"+a[1]],shell=True) #mapping
		if zuse == 1:
			p.wait()
		return 
	
	def sorting(self):
		a = self.setdir()
		subprocess.Popen("rm ./bam/*.indel",shell=True) 
		p = subprocess.Popen(["samtools sort -@ 40 -o "+a[2]+" "+a[1]],shell=True) #sort
		#p2.wait()
		#os.remove(a[1])
		return  
  
	def rmdup(self):
		a = self.setdir()
		p = subprocess.Popen(["samtools rmdup -s "+a[3]+" "+a[4]],shell=True) #remove duplications
		#p3.wait()
		#os.remove(a[3])
		return 
  
	def count(self):
		a = self.setdir()
		p = subprocess.Popen("bedtools coverage  -abam ./bed/bin_ucsc_hg19.bed -b "+a[4]+" > "+a[5],shell=True) 
		#p4.wait()
		#os.remove(a[4])
		return   
 
	def align(self,zuse = 0):
		cpu = psutil.cpu_percent(interval=1)
		if float(cpu) < 75.0:
			self.setdir()
			self.mapping()
			time.sleep(8)
		else:
			time.sleep(5)
			cpu = psutil.cpu_percent(interval=1) 
			while float(cpu) > 75.0:
				time.sleep(8)
				cpu = psutil.cpu_percent(interval=1) 
			else:
				self.setdir()
				self.mapping()
				time.sleep(8)
						
	def sort(self):
		cpu = psutil.cpu_percent(interval=1)
		if float(cpu) < 80.0:
			self.sorting()
			time.sleep(5)
		else:
			time.sleep(5)
			cpu = psutil.cpu_percent(interval=1) 
			while float(cpu) > 80.0:
				time.sleep(5)
				cpu = psutil.cpu_percent(interval=1) 
			else:
				self.sorting()
				time.sleep(5)
			
def onebyone(fq,filedir,method,waittime_1,waittime_2):
	for i in range(n):
		time.sleep(waittime_1)
		sample = nipt(fq[i],filedir)	
		if method == 0:
			sample.align()
		elif method == 1:
			sample.sort()
		elif method == 2:
			sample.rmdup()
		elif method == 3:
			sample.count()
	time.sleep(waittime_2)
	
#########>>> This is main process <<<###########
#n = 96				 
def main():
	print(range(n))
	i = datetime.datetime.now()
	map_time = str(i)[0:19]
	onebyone(fq_name,file_dir,0,0,200)
	i = datetime.datetime.now()
	sort_time = str(i)[0:19]
	onebyone(fq_name,file_dir,1,7,30)
	i = datetime.datetime.now()
	rmdup_time = str(i)[0:19]
	onebyone(fq_name,file_dir,2,20,220)
	i = datetime.datetime.now()
	counts_time = str(i)[0:19]
	onebyone(fq_name,file_dir,3,20,0)
	i = datetime.datetime.now()
	finish_time = str(i)[0:19]
	log.write('start time: '+start_time+"\r\n"+ \
	'mapping begin at: '+map_time+"\r\n"+ \
	'sorting begin at: '+sort_time+"\r\n"+ \
	'removing dup begin at: '+rmdup_time+"\r\n"+ \
	'counting begin at: '+counts_time+"\r\n"+ \
	'finish time: '+finish_time+' \r ')
################################################

#################>>> START <<<##################
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
log.close()



