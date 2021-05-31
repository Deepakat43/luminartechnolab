#we shd imprt frm functools
import functools

st=[9,7,5,6,4,1,2,3]
#reducing for getting sum of list
print(functools.reduce(lambda no1,no2:no1+no2,st))

#reducing to find highest no in list
print(functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,st))