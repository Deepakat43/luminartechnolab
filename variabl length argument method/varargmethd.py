def add(num1,num2):
    return num1+num2

res=add(10,20)
print(res)
#here 2 argumnts present

#what if there are 3,4,5 etc arguments present
#so we use ****variable length argument method****

def add(*args):
    print(args)
add(10)
add(10,20)
add(10,20,30,40,50)
#using this frmat we get argmnts in a (tuple) frmat


#fr getting sum frm tupe frmat :
def add(*args):
    res=0
    for num in args:
        res+=num
    return res
print(add(10,20,30,40,50))



