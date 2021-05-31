# lst=[2,3,4,5]
# print([num**2 for num in lst])
#
#
# list=["apple","orange","grape"]
# print([(fruit,fruit) for fruit in list])
#
# lst1=[10,20]
# lst2=[30,40]
# print([(num1,num2) for num1 in lst1 for num2 in lst2])
#
# #
# list=[1,2,3,4,5,6,7,8,9,10]
# print([num for num in list if num%2==0])

# list=[7,8,9,4,3,2]
# print([num+1 if num>5 else num-1 for num in list])

empyees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    {"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    {"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    {"eid":1004,"name":"ram","salary":20000,"designation":"nrkt"},
]
print([emp  for emp in empyees if emp["designation"]=="developer"])
print(max([emp["salary"] for emp in empyees]))