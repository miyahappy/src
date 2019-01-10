# coding=utf-8
import os,datetime,shutil,subprocess,time,re
os.chdir('/home/userroot/data/nipt')
ref_fasta = '/home/userroot/data/nipt/fa/hg38/Homo_sapiens_assembly38.fasta'
if(os.path.exists('./my_database')):
	shutil.rmtree('./my_database')
gvcf_name = os.listdir('./gvcf/')
#print(gvcf_name)
gvcf_file = []
for i in gvcf_name:
	if re.match('.*idx$',i) == None:
		gvcf_file.append(i)
		#print(i)
chr_name = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

def genomicsDB(chr_num,ref_fasta):
	if(os.path.exists('./'+chr_num)):
		shutil.rmtree('./'+chr_num)
	a = '~/software/gatk-4.0.4.0/gatk GenomicsDBImport  '
	b = ' -V ./gvcf/'
	c = ''
	d = ' --genomicsdb-workspace-path '+chr_num+' -L ' + chr_num
	for i in gvcf_file[0:10]:
		c = c + b + i
		#print(c)
	os.system(a+c+d)
	os.system('~/software/gatk-4.0.4.0/gatk GenotypeGVCFs -R '+ref_fasta+' -V gendb://'+chr_num+'  --use-new-qual-calculator -O /home/userroot/data/nipt/vcf/'+chr_num+'.vcf')

for i in chr_name:
	genomicsDB(i,ref_fasta)
