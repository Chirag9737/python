# two diffrent loops in python (1) For loop (2) While loop
  # (1) FOR loop
        # first inisilise value i=1
        # and declere termination condition

# for  i in range(1,10):
#     print(i)
# print(i)

    #  Q1 print element of a list using For loop


# list1 = ["CHIRAG","jikadra","age= 17"]

# for i in list1 :
#     print(i)


# (2) while loop 
  
# i = 2

# while i < 100:
#     print(i)
#     i+=2
# print(i)
    


# star petern in loop

# for n in range(5) :
#     print("*"" "*5)
#     # print(n)



# n = int(input("enter n : "))

# for i in range(n):
#      for j in range(1,n+1):
#         print(j,end=" ")
#      print()

# n = (int(input("enter n : ")))

# for i in range(1,n):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()




# n = (int(input("enter n : ")))


# for i in range(1,n+1):
#     print(" " * (n - i),end=" ")
#     for j in range(1,(2*i)):
#         print(j,end="")
#     print()

# n = int(input("enter n : "))

# for i in range(1,11):
#     print(n,' x ',i,"=", n*i)


#############################*&*^t^r############


# STAR PETTERNS 

# *
# **
# ***
# ****
# *****


# for i in range(6):
#     # print("*")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# ***
# **
# *

# for i in range(5):
#     print(i)
#     for j in range(i,5):
#         print("*",end=" ")
#     print()



#    *
#   **
#  ***
# ****

# for i in range(5):
#     for j in range(i,5):
#         print("",end=" ")
#     print((i+1)*"*",end="")
#     print()



# for i in range(5):
#     for j in range(i+1,5):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
        
# ****
#  ***
#   **
#    *

# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,5):
#         print("*",end=" ")
#     print()





for i in range(5):
    for j in range(i+1,5):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
    
for i in range(1,5):
    for j in range(i):
        print(" ",end="")
    for j in range(i+1,5):
        print("*",end="")
    for j in range(i,5):
        print("*",end="")
    print()
    
    
    
        
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    




