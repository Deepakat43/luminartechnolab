st=[7,8,10,4,3,2]

print(list(filter(lambda num:num%2==0,st)))


print(list(filter(lambda num:num>5,st)))




empyees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    {"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    {"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    {"eid":1004,"name":"ram","salary":20000,"designation":"nrkt"},
]

# print(list(filter(lambda emp:emp["designation"]=="developer",empyees)))
#
# #fr getting only names
# devp=list(filter(lambda emp:emp["designation"]=="developer",empyees))
# print(list(map(lambda emp:emp["name"],devp)))


print(list(map(lambda emp:emp["name"],list(filter(lambda emp:emp["designation"]=="developer",empyees)))))
