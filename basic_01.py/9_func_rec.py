# block of code & statement that perform to the spesific task

# func definetion

def cl_sum(a,b):
   s=(a+b)
   print(s)
   return s

print(cl_sum(5,6))   # fund call


def cl_sum(a =1,b = 2):
   s=(a+b)
   print(s)
   return s

print(cl_sum())   # fund call


def conveter(usd_val):
    inr_val = usd_val * 83
    print(usd_val , "USD =" ,inr_val,"INR")
    return inr_val
print(conveter(int(input("enter a dollar : " ))))



def numbers(n):
    if n % 2 == 0 :
        print("nuber is : Even")
    else :
        print("numbe is : Odd")
    return " even" if n%2==0 else "odd"

 
print(numbers(int(input("Enter your num : "))))


###########################################################################################


# recursion

 # when a function calls itself repeatedly
 # all the loop works == recursion works

def show(n):
    if n == 0:  # thie called base case
       return
    print(n)
    show(n-1)
    return  n

show(5)



def fact(n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * fact(n-1)

print(fact(5))

#############################################################
# practice


def sum_of(n):
    if n == 0:
        return 0
    sum = sum_of(n-1) + (n)
    return sum
print(int(sum_of(5)))

 

def print_list(list,idx=0):
    if idx == len(list):
        return 
    print(list[idx])
    return  print_list(list,idx+1)


chi = ["chirag","jikadra"]
print(print_list(chi))
















