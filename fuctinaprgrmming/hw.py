# st1=[7,8,9,4,3,1]
# st2=[]
# st3=[]
# for i in st1:
#     if i>5:
#         i+=1
#         st2.append(i)
#     else:
#         i-=1
#         st3.append(i)
# for j in st3:
#     st2.append(j)
# st1=st2
# print(st1)
#
#
#
#
#
st1=[10,20,21,22,23]
st2=[20,21,10,22,23]
a=set(st1)
b=set(st2)
if a==b:
    print("both list are equal")
else:
    print("lists are not equal")