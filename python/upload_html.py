# coding=gbk
########copy sequencing information files###########
import os,re,shutil
os.chdir("/home/cyto/nipt_back_up")

a = os.listdir("./fq")
for i in a:
	if re.match(".*sult",i, flags=0) == None:
		a.remove(i)
target_html = './files/html/'
target_fixed = './files/'
target_log = './files/log/'
target_qc = './files/fastqc/'
lane = ['L01','L02']
file_type =['allCycleHeatmap.html','bestFovReport.html','heatmapReport.html','summaryReport.html']
fixed_type = ['BarcodeStat.txt','BasecallQC.txt','FileName.txt','finish.signal','jsondata.txt','SequencingInfo.csv','summaryTable.csv']
def copy_html(a,lane,target_dir,file_type,rm):
	'''origin files will be deleted when rm = True !!!!'''
	width = len(a)
	for i in range(width):
		fcl = a[i][39:50]	
		print(a[i][0:-7])
		file_name = a[i][0:-7]+'_'+fcl+'_'+lane+'.'+file_type
		dir_fq = "./fq/" + a[i] + "/" + fcl +'/'+lane+'/'
		file_dir = dir_fq+file_name
		#print(str(k)+'/'+str(60)+'----'+file_name)
		shutil.copyfile(file_dir,(target_dir+file_type+'/'+file_name))
		if rm ==True:
			os.remove(file_dir) 
def copy_fixed(a,lane,target_dir,file_type,rm):
	'''origin files will be deleted when rm = True !!!!'''
	width = len(a)
	for i in range(width):
		fcl = a[i][39:50]	
		file_name = file_type
		dir_fq = "./fq/" + a[i] + "/" + fcl +'/'+lane+'/'
		file_dir = dir_fq+file_name
		print(file_dir)
		shutil.copyfile(file_dir,(target_dir+file_type+'/'+fcl+'_'+lane+'_'+file_name))
		if rm ==True:
			os.remove(file_dir)
def copy_log(a,lane,target_dir,rm):
	'''origin files will be deleted when rm = True !!!!'''
	width = len(a)
	for i in range(width):
		fcl = a[i][39:50]
		file_name = 'log_'+fcl+'_'+lane[2]+'.txt'
		dir_fq = "./fq/" + a[i] + "/" + fcl +'/'+lane+'/'
		file_dir = dir_fq+file_name
		print(file_dir)
		shutil.copyfile(file_dir,(target_dir+'/'+file_name))
		if rm ==True:
			os.remove(file_dir)
def copy_qc(a,lane,target_dir,rm):
	'''origin files will be deleted when rm = True !!!!'''
	width = len(a)
	for i in range(width):
		fcl = a[i][39:50]
		dir_fq = "./fq/" + a[i] + "/" + fcl +'/'+lane+'/'
		if os.path.exists(target_dir+fcl+'/') == False:
			os.mkdir(target_dir+fcl+'/')
		if os.path.exists(target_dir+fcl+'/'+lane+'/') == False:
			os.mkdir(target_dir+fcl+'/'+lane+'/')
		b = os.listdir(dir_fq)
		#print(b)
		for j in b:
			if j[-3:-1] == '.g':
				b.remove(j)
				#print(j)
		for j in b:
			if j[-3:-1] == '.g':
				b.remove(j)
				#print(j)
		for j in b:
			if j[-3:-1] == '.g':
				b.remove(j)
				#print(j)	
		#print(b)
		for j in b:	
			file_name = j	
			file_dir = dir_fq+file_name
		#print(file_dir)
			shutil.copyfile(file_dir,(target_dir+fcl+'/'+lane+'/'+file_name))
		if rm ==True:
			os.remove(file_dir)
#########copy files###########	
##fixed_file	
#for i in range(0,7):
#	copy_fixed(a,lane[0],target_fixed,fixed_type[i],rm=True)
#	copy_fixed(a,lane[1],target_fixed,fixed_type[i],rm=True)	
##log	
#copy_log(a,lane[0],target_log,rm=True)
#copy_log(a,lane[1],target_log,rm=True)	
##html					
#for i in range(0,4):
#	copy_html(a,lane[0],target_html,file_type[i],rm=True)
#	copy_html(a,lane[1],target_html,file_type[i],rm=True)
##fastqc
copy_qc(a,lane[0],target_qc,rm=False)
copy_qc(a,lane[1],target_qc,rm=False)
