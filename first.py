# l1=[1,4,9,16,25,36,49,64,81,100]
# x=int(input("Enter no:"))
# i=0
# while i < len(l1):
#     if (l1[i]== x):
#         print("Found at index",i)
#     i += 1

# i=0
# while i<=10:
#     if i%2 == 0:
#         i+=1
#         continue
#     print(i)
#     i+=1


# i=0
# while i<=10:
#     if i%2 != 0:
#         i+=1
#         continue
#     print(i)
#     i+=1

# l1=(1,4,9,16,25,36,49,64,81,100,36)
# x=36
# idx=0
# for i in l1:
#     if(i == x):
#         print("Found at index",idx)
#     idx += 1

# n=int(input("Enter the number: "))
# for i in range(1,11):
#     print(n," X ",i," = ",i*n)

# n=7
# sum=0
# i=1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# n=int(input("Enter the no: "))
# fact=1
# for i in range(1,n+1):
#     fact *= i
    
# print (fact)

# A=int(input("Enter NO.A: "))
# B=int(input("Enter NO.B: "))
# C=int(input("Enter NO.c: "))

# def cal_avg(A,B,C):
#     sum=A+B+C
#     avg=sum / 3
#     print(avg)
#     return avg

# cal_avg(A,B,C)

# l1=[1,4,9,16,25,36,49,64,81,100]
# def cal_len(l1):
#     length=len(l1)
#     print(length)
#     return length

# cal_len(l1)

# l1=[1,4,9,16,25,36,49,64,81,100]
# def show(list):
#     print(l)

# def print_el(list):
#     for el in list:
#         print(el, end=" ")

# print_el(l1)

# n=int(input("Enter the no: "))

# def find_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# find_fact(n)

# Rup=int(input("Enter Dollars: "))
# def convert(Rup):
#     conv=Rup*85.79
#     print(conv)

# convert(Rup)

# n=int(input("Enter no: "))
# def even_odd(n):
#     if n%2==0:
#         print("It is even")
#     else:
#         print("It is odd")

# even_odd(n)

# n=int(input("Enter no: "))
# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     return fact(n-1) * n

# print(fact(n))

# n=int(input("Enter the no: "))
# def calc_sum(n):
#     if (n == 0):
#         return 0
#     return calc_sum(n-1) + n

# print(calc_sum(n))

# l1=[1,4,9,16,25,36,49,64,81,100]
# def print_el(l1,idx=0):
#     if (idx == len(l1)):
#         return 
#     print(l1[idx])
#     print_el(l1,idx+1)

# print(print_el(l1))      

# Using Recursion 
# def factorial(n):
#     if ( n==0) or (n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# Using Recursion
# def fibonic(n):
#     if (n==1):
#         return 1
#     else:
#         return n + fibonic(n-1)
# print(fibonic(5))  
#                
# 
# 
# 
# 
# 
#  