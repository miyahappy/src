# -*- coding: utf-8 -*-
#import redis,csv
#import  pandas as pd
import xlrd
import json
import redis
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
pool = redis.ConnectionPool(host="192.168.5.252",port=6379,db=0)
r = redis.Redis(connection_pool=pool)

#name = str(raw_input("Enter sample id:"))
rowname = ['样本编号','样本类型','运输条件','取样日期','收样日期','孕周','胎儿类型','管道类型','原样本编号','姓名','身份证号','出生日期','年龄','门诊号'	,'送检医院','送检医生','身高','体重','联系地址','家庭电话','手机号码','紧急联系人','关系','联系人电话','预产期','末次月经','绒毛膜','唐筛结果','B超检查结果','是否IVF','分娩史孕次','分娩史产次','分娩史其他','羊水穿刺','既往史','现病史','过敏史','家族遗传病史','备注']
name = '18B0031234'
display_rowname = [rowname[6]]+[rowname[4]]+[rowname[5]]+[rowname[9]] + rowname[11:15]+ [rowname[20]] + [rowname[25]]
query = r.hmget('"'+name+'"',display_rowname)	
#print(r.hmget(a,rowname[3]).decode("unicode_escape").encode("gbk"))
#query = json.dumps(query, encoding='utf-8', ensure_ascii=False)
#print(query)
#print(type(query))
#query = query.split(',')
#print(query)
#print(type(query[0]))
#print(display_rowname)
for i in range(1,len(display_rowname)):
	#print(display_rowname[i].decode('gbk'))
	#print(query[i])
	display = display_rowname[i].decode('gbk') + ': ' + query[i]# + '\n'
	print(display)

#print(query)
#all_hash = r.hgetall(a)
#all_hash = json.dumps(all_hash, encoding='utf-8', ensure_ascii=False)
