# -*- coding: utf-8 -*-
#import redis,csv
#import  pandas as pd
import xlrd
import json
import redis
pool = redis.ConnectionPool(host="192.168.5.252",port=6379,db=0)
r = redis.Redis(connection_pool=pool)

#r.hmset("18B0011987",{"����":"��ĳĳ","����":"32","���":"�ͷ���"})
#result = r.hmget("18B0011987","����","����","���")
#for i in result:
#	i = i.decode('utf-8')
#	print(i)

	
workbook = xlrd.open_workbook('/home/userroot/data/nipt/20180808.xls')

#workbook = xlrd.open_workbook(r'E:/bioinformatics/mysql/������������_CL100090642_20180921_2018181.xls')
#sheetName = workbook.sheet_names()
sample = workbook.sheet_by_index(0)
nRows = sample.nrows
print(nRows)
sheet = ['1']
#for i in sheetName:
#	data = i.encode('gbk')
	#print(data)
#	sheet.append(data)
	#print(sheet) 
#print(sample)
#rowname = str(sample.row_values(0)).decode("unicode_escape").encode("gbk")
#print(rowname)
#print(len(rowname))
rowname = ['�������','��������','��������','ȡ������','��������','����','̥������','�ܵ�����','ԭ�������','����','���֤��','��������','����','�����'	,'�ͼ�ҽԺ','�ͼ�ҽ��','���','����','��ϵ��ַ','��ͥ�绰','�ֻ�����','������ϵ��','��ϵ','��ϵ�˵绰','Ԥ����','ĩ���¾�','��ëĤ','��ɸ���','B�������','�Ƿ�IVF','����ʷ�д�','����ʷ����','����ʷ����','��ˮ����','����ʷ','�ֲ�ʷ','����ʷ','�����Ŵ���ʷ','��ע']


for i in range(1,nRows):
	row = sample.row_values(i)#.decode("unicode_escape").encode("gbk")
	#print(row[1])
	#row = json.dumps(row, encoding='gbk', ensure_ascii=False)
	inputData = {rowname[1]:row[1]}
	#inputData = dict(zip(rowname[1],row[1]))
	for j in range(1,len(rowname)):
		inputData[rowname[j]] = row[j]
	a = '"'+row[0]+'"'
	#inputData = json.dumps(inputData, encoding="gbk", ensure_ascii=False, sort_keys=False, indent=4)
	#print(inputData)
	#print(isinstance(inputData,dict))
	r.hmset(a,inputData)
	#print(row[0])
#print(isinstance(a,list))
name = str(raw_input("Enter sample id:"))
query = r.hmget('"'+name+'"',rowname[9])	
#print(r.hmget(a,rowname[3]).decode("unicode_escape").encode("gbk"))
query = json.dumps(query, encoding='utf-8', ensure_ascii=False)
print(query)
all_hash = r.hgetall(a)
all_hash = json.dumps(all_hash, encoding='utf-8', ensure_ascii=False)
	#print(all_hash)
#a = {rowname[1]:row[1],rowname[2]:row[3],rowname[4]:row[4],rowname[5]:row[5]}
#a = dict(a)
#print(a)
#print(isinstance(a,dict))

