# # section 5
# #5.1

# a= int (input("Enter first number: "))
# b= int (input("Enter second number: "))
# if a>b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")
# #5.2

# n=int (input("Enter a number: "))   
# if n%2==0:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")

# #5.3
# n=int(input("Enter a number: "))
# for i in range(2,n//2+1):
#     if n%i==0:
#         print(f"{n} is not prime")
#         break
# else:
#      print("Prime")


# #5.4
# a=input("Enter First String: ")
# b=input("Enter Second String: ")
# if a==b:
#     print ("The strings are equal")
# else:
#     print ("The strings are not equal")
# #Assignment 5.1
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# print("MAX of the numbers is: ", max(a,b,c))

# #assignment 5.2
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if i%7==0 and i%9==0:
#         sum=sum+i

# print("The sum of numbers divisible by 7 and 9 is: ", sum)


# #assignment 5.3 WAP to add all prime numbers from 1 to n and n is given by the user.
# n=int(input("Enter a number: "))
# sum=0
# for i in range(2,n+1):
#     for j in range(2,i//2+1):
#         if i%j==0:
#             break
#     else:
#         sum=sum+i
# print("The sum of prime numbers from 1 to ", n, " is: ", sum)


# #Function
# #assignment 6.1
# n=int(input("Enter a number: "))
# def add_odd(n):
#     sum=0;
#     for i in range(1,n+1):
#         if i%3==0:
#             sum=sum+i
#     return sum


# print("The sum of numbers divisible by 3 from 1 to ", n, " is: ", add_odd(n))


#assignment 6.2

n=int(input("Enter a number: "))
def prime_sum(n):
    sum=0
    for i in range(2,n+1):
        for j in range(2,i//2+1):
          if i%j==0:
            break
        else:
             sum=sum+i
    return sum
print("The sum of prime numbers from 1 to ", n, " is: ",prime_sum(n))