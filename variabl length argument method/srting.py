# arr=[10,8,11,9,12]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)
# data1=sorted(arr,reverse=True)
# print(data1)
# data2=sorted(arr)
# print(data2)


# def emp(**kwargs):
#     print(kwargs)
# emp(id=150151,name="deep",amnt=50000)



empyees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001:{"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    1002:{"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    1003:{"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    1004:{"eid":1004,"name":"ram","salary":20000,"designation":"nrkt"},

}
def emp(**kwargs):
    id=kwargs["id"]
    prp=kwargs["prp"]
    if id in empyees:
        print(empyees[id]["name"])
        print(empyees[id][prp])
    else:
        print("NA")
emp(id=1003,prp="designation")




