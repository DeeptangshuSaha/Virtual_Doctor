import csv
import pandas as pd
import os
trial='this is a try'
#_____________________________________________
def common_member(a):
        l=[]
        res=[key for key in a.keys()]
        for i in res:
                l=l+a[i]
        b=list(set(l))
        return b        
#_____________________________________________     
def dis(sym):
    d={}
    for i in sym:
        csv_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
        v=open(csv_path,"r")
        df=csv.reader(v,delimiter=",")
        dt=[]
        for j in df:
            for k in j[1:]:
                if i in k:
                    dt.append(j[0])
                    break
        d[i]=dt
    ls=[]
    f=common_member(d)
    return f
    '''for p in d.values():
        ls.append(p)
    return ls'''
#_____________________________________________
def starter(alist):
    lit=dis(alist)
    return lit
if __name__ == '__main__':
    starter()