st=[2,3,4,5,6,7]
print(list(map(lambda num:num**2,st)))


name=["ajay","aravind","arun"]
print(list(map(lambda string:string.upper(),name)))


st=[6,7,8,4,3,2,1]
print(list(map(lambda num:num+1 if num>5 else num-1,st)))



empyees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    {"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    {"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    {"eid":1004,"name":"ram","salary":20000,"designation":"nrkt"},
]
print(list(map(lambda emp:emp["name"],empyees)))
print(list(map(lambda emp:emp["salary"],empyees)))

