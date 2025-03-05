# num1 = float(input("Enter the first number for addition: "))
# num2 = float(input("Entet the second number for addition: "))
# sum_result = num1 + num2
# print(sum_result)


# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year,month)
# print(cal)


# prime number

# num = int(input("Enter a number: "))
# flag = False

# if num==1:
#     print("not a prime number")
  

# elif num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             flag=True
#             break
# if flag:
#     print("num is not prime number--")
# else:
#     print("number is prime number--")





# Armstrong Number


# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digits = len(num_str)
# temp_num = num

# sum_of_power = 0
# while temp_num >0:
#     digit = temp_num%10
#     sum_of_power = sum_of_power + digit**num_digits
#     temp_num = temp_num // 10

# if sum_of_power == num:
#     print("arm strong")
# else:
#     print("not a arm strong")


def f(a,L=[]):
    L.append(a)
    return L

l1=f(1)
l2=f(2)
l3=f(3)
print(l3)
