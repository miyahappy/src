# coding=gbk
########copy slected fq###########
#import numpy as np
import pandas as pd
import os,re,shutil,csv
os.chdir("/home/cyto/nipt_back_up")
#data = pd.read_csv(r"nipt_hbv.csv")
#data = csv.reader(open("nipt_hbv.csv"))
#data = data[['sample_id','fcl','lane','barcode']]
a = os.listdir("./fq")
for i in a:
	if re.match(".*sult",i, flags=0) == None:
		a.remove(i)
target = './files/html/'
width = len(a)
k=0
lane = ['L01','L02']
file_type =['allCycleHeatmap.html','bestFovReport.html','heatmapReport.html','summaryReport.html']
def copy_html(a,lane,target_dir,file_type):
	width = len(a)
	for i in range(width):
		fcl = a[i][39:50]	
		print(a[i][0:-7])
			#file_name = fcl+'_'+lane+'_'+str(barcode)+'.fq.gz'
		file_name = a[i][0:-7]+'_'+fcl+'_'+lane+'.'+file_type
		dir_fq = "./fq/" + a[i] + "/" + fcl +'/'+lane+'/'
		file_dir = dir_fq+file_name
		#print(str(k)+'/'+str(60)+'----'+file_name)
		shutil.copyfile(file_dir,(target_dir+file_type+'/'+file_name))
for i in range(0,4):
	copy_html(a,lane[0],target,file_type[i])
	copy_html(a,lane[1],target,file_type[i])
