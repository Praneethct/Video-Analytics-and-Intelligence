import requests
import json
import datetime

url='https://face-roll.firebaseio.com/'

def insert(fv):
    now=datetime.datetime.now()
    data={now.strftime("%H:%M:%S:%f"):{'camera':1,'features':fv}}
    requests.patch(url+'{0}.json'.format(now.strftime("%d-%m-%Y")),json.dumps(data))

def retrive(date,from_time,to_time):
    ftm=datetime.datetime.strptime(date+' '+from_time,'%d-%m-%Y %H:%M')
    ttm=datetime.datetime.strptime(date+' '+to_time,'%d-%m-%Y %H:%M')
    descriptors=[]
    data=requests.get(url+'{0}.json'.format(date)).json()
    #print(data)
    for dt in data:
        print('for loop')
        datm=datetime.datetime.strptime(date+' '+dt,'%d-%m-%Y %H:%M:%S:%f')
        print(ftm)
        print(datm)
        print(ttm)
        if (ftm<=datm)&(datm<=ttm):
            print('loop')
            descriptors.append(data['{0}'.format(datm.strftime("%H:%M:%S:%f"))]['features'])
    return descriptors
