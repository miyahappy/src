# -*- coding: utf-8 -*-
#import redis,csv
#import  pandas as pd
import xlrd
import json
import redis
pool = redis.ConnectionPool(host="192.168.5.252",port=6379,db=0)
r = redis.Redis(connection_pool=pool)

#r.hmset("18B0011987",{"姓名":"王某某","年龄":"32","结果":"低风险"})
#result = r.hmget("18B0011987","姓名","年龄","结果")
#for i in result:
#	i = i.decode('utf-8')
#	print(i)

	
workbook = xlrd.open_workbook('/home/userroot/data/nipt/20180808.xls')

#workbook = xlrd.open_workbook(r'E:/bioinformatics/mysql/样本分析数据_CL100090642_20180921_2018181.xls')
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
rowname = ['样本编号','样本类型','运输条件','取样日期','收样日期','孕周','胎儿类型','管道类型','原样本编号','姓名','身份证号','出生日期','年龄','门诊号'	,'送检医院','送检医生','身高','体重','联系地址','家庭电话','手机号码','紧急联系人','关系','联系人电话','预产期','末次月经','绒毛膜','唐筛结果','B超检查结果','是否IVF','分娩史孕次','分娩史产次','分娩史其他','羊水穿刺','既往史','现病史','过敏史','家族遗传病史','备注']


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

