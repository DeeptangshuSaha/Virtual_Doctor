import csv
import pandas as pd


def common_member(a):
        l=[]
        res=[key for key in a.keys()]
        for i in res:
                l=l+a[i]

        b=list(set(l))
        print(b)
        
                

def dis(sym):
    global d
    d={}
    for i in sym:
        v=open("dataset.csv","r")
        df=csv.reader(v,delimiter=",")
        dt=[]
        for j in df:
            for k in j[1:]:
                if i in k:
                    dt.append(j[0])
                    break
        d[i]=dt
        
    ls=[]

    common_member(d)
    #print(d,'a')
    
    for p in d.values():
        ls.append(p)
    return ls



st=""
lst=eval(input('Enter list of Symptoms:' ))
#lst=[]
'''while st=="":
    inp=input("ENTER SYMPTOM : ")
    ip=inp.lower()
    lt=ip.split(" ")
    inp="_".join(lt)
    lst.append(inp)
    q=input("Any other symptom ? ")
    if q=="no" or q=="No" or q=="NO" or q=='n' or q=='N':
        st="ok"   '''
lit=dis(lst)

for a in range (len (lit)):
    if a==0:
        lst1=lit[0]
        uni=lst1
    else:
        lst2=lit[a]
        ins=list(set(lst1) & set(lst2))
        lst1=ins
        uni=list(set(uni) | set(lst2))
if len(lst1)==0:
    with open("data.csv","w") as f:
        rec=csv.writer(f,delimiter=",")
        print("Couldn't find any particular disease(s)")
        rec.writerow(["WE SUSPECT"])
        for i in uni:
            rec.writerow([i])
            
else:
    with open("data.csv","w") as f:
        rec=csv.writer(f,delimiter=",")
        rec.writerow(["Possible Illness(es)"])
        for b in lst1:
            rec.writerow([b])
    rd=pd.read_csv("data.csv")

