# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
from django.http import HttpResponse
sys.path.append('C:\\Users\\2017SEa\\Desktop\\Django_Template_python2-master\\Django\\myproject\\DemoProject\\models')
import MySQL_model as sql
import json

###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'stringData': str(datetime.now()),}
    return render(request,template,responds )


def UsingStaticSource(request):
    template = 'UsingStaticSource.html'
    responds = {}
    return render(request,template,responds )

def For_Cycle(request):
    template = 'For_Cycle.html'
    arr = [1,2,3,4,5,6,7,8,9]
    responds = {'Data':arr}
    return render(request,template,responds )

def Http_From_Get(request,input1,input2):
    template = 'hello_world.html'
    responds = {'stringData': str(input1)+str(input2),}
    return render(request,template,responds )

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def Http_From_Post(request):
    try:
        data = str(request.POST['input1'])
    except KeyError as e:
        data = 'did not have post'


    template = 'Form.html'
    responds = {'stringData': data,}
    return render(request,template,responds )



########################
@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def Who_am_I(request):
    sql.connectDB()
    try:
        uid = str(request.POST['uid'])
        psw = str(request.POST['psw'])
        #data = str(uid)+str(psw)
        sqlcmd="SELECT * FROM `user` WHERE `U_id` = '"+str(uid)+"' AND `U_pwd` = '"+str(psw)+"'"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        data = 'Input error'

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)


@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def import_vegetable(request):
    # sample data = [   {     "交易日期": "106.12.25",     "作物代號": "rest",     "作物名稱": "休市",     "市場代號": "104",     "市場名稱": "台北二",     "上價": 0.0,     "中價": 0.0,     "下價": 0.0,     "平均價": 0.0,     "交易量": 0.0   },   {     "交易日期": "106.12.25",     "作物代號": "FA001",     "作物名稱": "康乃馨-混合色",     "市場代號": "105",     "市場名稱": "台北市場",     "上價": 35.0,     "中價": 35.0,     "下價": 35.0,     "平均價": 35.0,     "交易量": 30.0   }]
    sql.connectDB()
    try:
        jsondata = str(request.POST['jsondata'])
        try:
            A_id = str(request.POST['A_id'])
        except:
            A_id = "1"
        d = json.loads(jsondata) 
        
        data = 'success'
        for raw in d:
            
            V_id = str(raw['作物代號'])
            V_name = str(raw['作物名稱'])
            V_area = str(raw['市場名稱'])
            try:
                
                sqlcmd="INSERT INTO `vegetable` (`V_id`, `V_name`, `V_area`) VALUES ('"+V_id+"', '"+V_name+"', '"+V_area+"');"
                print(sqlcmd)
                print(sql.exeSQl(sqlcmd))
            except Exception as e:
                print(e)



            ####
            #INSERT INTO `vegetable_price` (`P_id`, `V_id`, `P_date`, `A_id`, `P_h`, `P_m`, `P_l`, `P_avg`) VALUES (NULL, 'rest', CURRENT_TIMESTAMP, '1', '0.0', '0.0', '0.0', '0.0');
            date = str(raw['交易日期']).split(".")
            P_date= str(1911+int(date[0]))+'-'+str(date[1])+'-'+str(date[2])+' 12:00:00'
            #A_id = str(raw['作物代號'])
            P_h = str(raw['上價'])
            P_m = str(raw['中價'])
            P_l = str(raw['下價'])
            P_avg = str(raw['平均價'])
            try:
                
                sqlcmd="INSERT INTO `vegetable_price` (`P_id`, `V_id`, `P_date`, `A_id`, `P_h`, `P_m`, `P_l`, `P_avg`) VALUES (NULL, '"+V_id+"', '"+P_date+"', '"+A_id+"', '"+P_h+"', '"+P_m+"', '"+P_l+"', '"+P_avg+"');"
                print(sqlcmd)
                print(sql.exeSQl(sqlcmd))
            except Exception as e:
                print(e)
    except KeyError as e:
        data = 'Input error'
    
    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)


@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def search_price_by(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    data='error'
    try:
        vid = str(request.POST['vid'])
        
        #data = str(uid)+str(psw)
        sqlcmd="SELECT * FROM `vegetable_price` WHERE `V_id` = '"+str(vid)+"'"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        pass
    try:#SELECT * FROM `vegetable` WHERE `V_name` LIKE '%青%'
        v_name = str(request.POST['vname'])
        
        #data = str(uid)+str(psw)
        sqlcmd="SELECT `V_id` FROM `vegetable` WHERE `V_name` LIKE '%"+v_name+"%'"
        
        vid = sql.exeSQl(sqlcmd)
        print(sqlcmd)

        sqlcmd="SELECT * FROM `vegetable_price` WHERE `V_id` = '"+str(vid[0][0])+"'"
        print(sqlcmd)
        data = sql.exeSQl(sqlcmd)
        
    except Exception as e:
        print(e)

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def get_vegetable_by_id(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    
    try:
        vid = str(request.POST['vid'])
        
        #data = str(uid)+str(psw)
        sqlcmd="SELECT * FROM `vegetable` WHERE `V_id` = '"+str(vid)+"'"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        data='error'
    

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)

#INSERT INTO `follow` (`id`, `U_id`, `V_id`, `A_id`) VALUES (NULL, 'testa1', 'FA001', '1');

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def follow_vegetable(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    
    try:
        uid = str(request.POST['uid'])
        vid = str(request.POST['vid'])
        aid = str(request.POST['aid'])
        #data = str(uid)+str(psw)
        sqlcmd="INSERT INTO `follow` (`id`, `U_id`, `V_id`, `A_id`) VALUES (NULL, '"+uid+"', '"+vid+"', '"+aid+"');"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        data='error'
    

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)

#INSERT INTO `report` (`id`, `U_id`, `V_id`, `A_id`, `R_date`) VALUES (NULL, 'testa1', 'FR1', '1', CURRENT_TIMESTAMP);
@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def report_vegetable_price(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    
    try:
        uid = str(request.POST['uid'])
        vid = str(request.POST['vid'])
        aid = str(request.POST['aid'])
        price = str(request.POST['price'])

        #data = str(uid)+str(psw)
        sqlcmd="INSERT INTO `report` (`id`, `U_id`, `V_id`, `A_id`, `R_date`, `price`) VALUES (NULL, '"+uid+"', '"+vid+"', '"+aid+"', CURRENT_TIMESTAMP, '"+price+"');"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        data='error'
    

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def get_reported_price(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    data='error'
    try:
        vid = str(request.POST['vid'])
        
        #data = str(uid)+str(psw)
        sqlcmd="SELECT * FROM `report` WHERE `V_id` = '"+str(vid)+"'"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        pass
    

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)



#UPDATE `report` SET `r_abort` = '0' WHERE `report`.`id` = 3;

@csrf_exempt #csrf skip, if you want to get the http's post form anywhere
def abort_report(request):#SELECT * FROM `vegetable_price`
    sql.connectDB()
    data='error'
    try:
        tid = int(request.POST['tid'])
        
        #data = str(uid)+str(psw)
        sqlcmd="UPDATE `report` SET `r_abort` = '0' WHERE `report`.`id` = "+str(tid)+";"
        
        data = sql.exeSQl(sqlcmd)
        
    except KeyError as e:
        pass
    

    sql.close()
    #template = 'Form.html'
    #responds = {'stringData': data,}
    return HttpResponse(data)