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
rowname = ['�������','��������','��������','ȡ������','��������','����','̥������','�ܵ�����','ԭ�������','����','���֤��','��������','����','�����'	,'�ͼ�ҽԺ','�ͼ�ҽ��','���','����','��ϵ��ַ','��ͥ�绰','�ֻ�����','������ϵ��','��ϵ','��ϵ�˵绰','Ԥ����','ĩ���¾�','��ëĤ','��ɸ���','B�������','�Ƿ�IVF','����ʷ�д�','����ʷ����','����ʷ����','��ˮ����','����ʷ','�ֲ�ʷ','����ʷ','�����Ŵ���ʷ','��ע']
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
