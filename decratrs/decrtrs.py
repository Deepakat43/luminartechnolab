#
# def shuffle_values(func):
#     def wrapper(no1,no2):
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#         return func(no1,no2)
#     return wrapper
#
#
# @shuffle_values
# def div(no1,no2):
#     return no1/no2
# print(div(5,10))
#
#
#
#
# @shuffle_values
# def sub(no1,no2):
#     return no1-no2
# print(sub(5,10))


# def admin_required(func):
#     def wrapper(user,pin):
#         if (user!="admin"):
#             raise Exception("NO AUTHERISATION")
#         else:
#             return func(user,pin)
#     return wrapper
#
# @admin_required
# def change_pin(user,pin):
#         mypin=pin
#         return mypin
#
# @admin_required
# def acc_delete(user,acc):
#     return str(acc)+"deleted"
#
# try:
#     print(change_pin("admin",12313))
# except Exception as e:
#     print(e.args)
#
#
# try:
#     print(acc_delete("admin",654659452))
# except Exception as e:
#     print(e.args)


def vcntn_portal(**kwargs):
    print(kwargs)

vcntn_portal(name="ram",age=25,address="address",health_issues=True)
