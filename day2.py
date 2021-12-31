"""
作者：YuanMengna
日期：2021年12月15日
"""
"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and
 generate a list and a tuple which contains every number.
 Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input.
tuple() method can convert list to tuple
"""
# my answer
# a=()
# b=[]
# c=input("请输入一串数字：")
# c.split(',')
#
# #answer：
# lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
#                           # method name split. ',' inside split function does split where it finds any ','
#                           # and save the input as list in lst variable
#
# tpl = tuple(lst)          # tuple method converts list to tuple
#
# print(lst)
# print(tpl)

"""Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters"""
# my answer:
# class String():
#     def __init__(self):
#         pass
#
#     def Getstring(self):
#         self.s=input("请输入一串字符：")
#
#     def Printstring(self):
#         print(self.s.upper())
# # the answer:
# # class IOstring():
# #     def get_string(self):
# #         self.s = input()
# #
# #     def print_string(self):
# #         print(self.s.upper())
#
# xx = String()
# xx.Getstring()
# xx.Printstring()


"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value 
(for example, if the output received is 26.0, it should be printed as 26).
In case of input data being supplied to the question, 
it should be assumed to be a console input."""
# my version of answer:
# a = (input("请输入三个整数：").split(','))
# print(a)
# for i in a:
#     b=int(i)
#     num = int((((2*50*b)/30)**0.5))
#     print(num)


# others' answer:
from math import sqrt # import specific functions as importing all using *
                      # is bad practice

# C,H = 50,30
#
# def calc(D):
#     return sqrt((2*C*D)/H)
#
# D = [int(i) for i in input().split(',')]  # splits in comma position and set up in list
# D = [int(i) for i in D]   # converts string to integer
# D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
# D = [round(i) for i in D] # All the floating values are rounded
# D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation
# print(",".join(D))


# # others' answer:
# from math import sqrt
#
# C,H = 50,30
#
# def calc(D):
#     return sqrt((2*C*D)/H)
#
# D = input().split(',')                     # splits in comma position and set up in list
# D = [str(round(calc(int(i)))) for i in D]  # using comprehension method.
# # It works in order of the previous code
# print(",".join(D))
#
# # others' answer:
# from math import * # importing all math functions
# C,H = 50,30
#
# def calc(D):
#     D = int(D)
#     return str(int(sqrt((2*C*D)/H)))
#
# D = input().split(',')
# D = list(map(calc,D))   # applying calc function on D and storing as a list
# print(",".join(D))
#
# # Quesion 7:
# my answer:
#
# def TwoD_array(a,b):
#     pass
#
# #
# # A = input("请输入两个用来创建数组的值：").split(',')
# # print(A)
# # B = [int(i) for i in A]
# # for i in B:
# #     for j in range(0,i):
# #
#
# solution 1:
# x,y = map(int,input().split(','))
# lst=[]
#
# for i in range(x):
#     tmp=[]
#     for j in range(y):
#         tmp.append(i*j)
#     lst.append(tmp)
#
# print(lst)
#
# solution2:
# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)


# Question 8
# my answer
# def Sort_order():
#     a=input("请输入一串字符：").split(',')
#     a.sort()
#     print(",".join(a))
#
# Sort_order()

# quetion 9:
def Convert():
    lst=[]
    while True:
        a = input("请输入几行字符")
        if len(a) != 0:
            lst.append(a.upper())
        else:
            break
    for line in lst:
        print(line)

Convert()



