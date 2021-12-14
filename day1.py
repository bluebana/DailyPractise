"""
作者：YuanMengna
日期：2021年12月14日
"""
"""
Question1:
Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method.
"""
# my version of answer:
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,",")

# correct answer:
# for i in range(2000,3201):
#     if i%7 == 0 and i%5!=0:
#         print(i,end=',')
# print("\b")

#what i learned:
#end的作用

"""Question 2
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 
Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
#my version of answer
#用while循环做：
# a=int(input("请输入一个整数:"))
# i=1
# b=1
# while i<(a+1):
#     b=i*b
#     i=i+1
# print(a,"的阶乘为",b)

#用for循环做：
# a=int(input("请输入一个整数:"))
# c=1
# for i in range(1,a+1):
#     c=i*i    #第一个错误在于循环在这里只是求平方 没有意义
#     print(c)  #第二个错误在于print应该打印最终结果，所以要取消缩进

#original answer:
# n = int(input()) #input() function takes input as string type
#                 #int() converts it to integer type
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# n = int(input()) #input() function takes input as string type
#                  #int() converts it to integer type
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i;
#     i = i + 1
# print(fact)


#Using Lambda Function
# n = int(input("请输入"))
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))


# n = int(input("请输入"))
# def shortfact(x):
#     if x<= 1:
#         return x
#     else:
#         return x*shortfact(x-1)
# print(shortfact(n))

"""
With a given integral number n, 
write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.
Consider use dict()
"""

# my solution
a=int(input("请输入一个整数："))
b={}

for i in range(1,a+1):
    b[i]=i*i
print(b)
#和答案差不多

#Using dictionary comprehension
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)