
def str_value(ste):
    sum=0
    list1=str.split(",")
    length1 = len(list1)
    dict_data = {1:"one",60:"sixty"}
    for i in range(0,length1):
        # print()
        # print(list1[i])
        sum=sum+int(list1[i])
    # if sum.keys() in dict_data:
    #     return
    return "you have entered {}".format(sum)

# str = "10,20,30"
str = input("please enter comma sepaerate integer: ")
# str_value(str)

print(str_value(str))

# temp_dict = {"emp_id":[1,2,3],
#              "name":["amit","sumit","raj"],
#              "salary":[12000,13000,14000]
#              }