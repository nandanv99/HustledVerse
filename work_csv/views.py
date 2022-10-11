from operator import index
from os import sep
from django.shortcuts import redirect, render
from sqlalchemy import column
# from work_csv.models import work_csv
# from media.data_csv import *
import pandas as pd
import sys


# Create your views here.


def home(request):
    return render(request,"index2.html")

def open_csv(request):
    return render(request,"upload.html")

def upload_csv(request):
    if request.method=='POST' and request.FILES['mycsv']:
        myfile = request.FILES['mycsv']

        file=request.FILES.get('mycsv')
        file1=file
        # cols=4
        # with open(sys.argv[1]) as file:
        #     for line in file:
        #         print("cool",'|'.join(line.strip().split('|')[:cols]))
        data=pd.read_csv(file1)
        # This is for columns names extraction
        columns=str(data.columns)
        columns=columns.replace("Index(['",'',100)
        columns=columns.replace("], dtype='object')",'',100)
        columns=columns.replace('|',',',100)
        list=columns.split(',')
        cols=list
        ######### end extraction #########
        # print(str(data.head))
        print(len(list))
        print(data.head(1))
        headdata1=data.loc[0].values.flatten().tolist()
        headdata2=data.loc[1].values.flatten().tolist()
        headdata3=data.loc[2].values.flatten().tolist()
        headdata4=data.loc[3].values.flatten().tolist()
        headdata5=data.loc[4].values.flatten().tolist()
    
        # for i in range(50):
        #     data_sets={}

        # for i in range(len(data)):
        #     name="col0"
        #     data_sets[name] = []
        #     # data_sets[name] = [data.iloc[:,[i]].values.flatten().tolist()]
        #     data_sets.update(name : data.iloc[:,[i]].values.flatten().tolist())
        #     name="col"+str(i+1)
        # print("data_sets : ",data_sets)


        param={'head':cols,'columns':len(cols),'row':len(data),
                'whole_data':cols[::],
                'col0_name':data.columns[0],
                'col1_name':data.columns[1],
                'col2_name':data.columns[2],
                'col3_name':data.columns[3],
                'col4_name':data.columns[4],
                'col0':data.iloc[:,[0]].values.flatten().tolist(),
                'col1':data.iloc[:,[1]].values.flatten().tolist(),
                'col2':data.iloc[:,[2]].values.flatten().tolist(),
                'col3':data.iloc[:,[3]].values.flatten().tolist(),
                'col4':data.iloc[:,[4]].values.flatten().tolist()
                ,'headdata1':headdata1,'headdata2':headdata2,
                'headdata2':headdata2,'headdata3':headdata3,'headdata4':headdata4}

        return render(request,"work_csv.html",param)
        # return render(request,"main.html",param)
    else:
        redirect('/')



