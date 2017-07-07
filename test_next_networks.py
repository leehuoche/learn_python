# -*- coding: utf-8 -*-

import sqlite3
import json
import sys
import os


log=open('data_log.txt','w')
#raise SystemExit
path='W:\Next_networks\\raw data'#这是py文件与raw_data放在一个文件夹中，这个path路径是raw_data 的路径。
names = [name for name in os.listdir(path) if name.endswith('.json')]#这个是我防止打出这个文件夹中的py文件。

#建立数据库

global id
id=0

#index是用来指示文件的次序。
index=1
#遍历文件，提取信息
for fn in names:
        file_list=fn
        fp=open(file_list,'r')
        data=json.load(fp)
        print '-'*18 ,index,'-'*18, fn
        index=index+1

        for item in data:
            id=id+1
            #没有异常的选项
            first=id
            second=int(item['msm_id'])
            fifth=int(item['timestamp'])
            sixth=int(item['prb_id'])
            ninth=str(item['proto'])

            #第7，8个异常：没有result
            try:    
                seventh=int(item['result']['size'])
                eighth=int(item['result']['rt'])                
            except:
                error_svn_eth=item['error'].keys()
                if(error_svn_eth==['timeout']):
                    status='timeout'
                else:
                    status='unknown'
            else:
                status='connected'

            status_1=status

            #第3个异常：from数据为空字符串，不触发异常
            
            third=str(item['from'])
                #print "third_try"
            if(len(third)<2):
                third="empty_from"
                #print "third_excp"*7
                error_third=item['error'].keys()
                if(error_third==['timeout']):
                    status='timeout'
                else:
                    status='unknown'
            else:
                status='connected'

            status_2=status

            #第4个异常：dst_addr没有键值
            try:
                fouth=str(item['dst_addr'])
                
            except:
                fouth='empty_dst'

                error_fouth=item['error'].keys()
                if(error_fouth==['timeout']):
                    status='timeout'
                else:
                    status='unknown'
            else:
                status='connected'

            status_3=status

            #第10个选项，status的判定。
            if(status_1=='timeout' or status_2=='timeout' or status_3=='timeout'):
                tenth='timeout'
            elif(status_1=='connected' and status_2=='connected' and status_3=='connected'):
                tenth='connected'
            else:
                tenth='unknown'
           
            print >>log,first,second,third,fouth,fifth,sixth,seventh,eighth,ninth,tenth
            


            #插入数据库
            #inst=(first,second,third,fouth,fifth,sixth,seventh,eighth,ninth,tenth)
            #conn.execute("INSERT INTO atlas VALUES(%s,%s,'%s','%s',%s,%s,%s,%s,'%s','%s');" %inst)
            #这里有个错误需要记录：字符串插入时候需要'%s'

