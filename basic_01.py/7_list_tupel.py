
# list allows us to store multipul items in a single varibal
# list have index stat from 0 to nnn , all data type is stor
#  nagetive indexing is posiable in python

marks = [92,65,65,32,85,95,96,]

print(marks[0:5]) # list slising S_index : End_index
print(len(marks)) # lenth in list
marks[0]= 99.99
print(marks[0])

# list methods 

marks.append(4)



marks.sort()

marks.sort(reverse=True)

marks.reverse()


# marks.extend() concatimate list ot  another list
marks.insert(8,55)

marks.pop(0)
marks.remove(55)
# marks.index(5)
marks.copy()
print (marks)




# tupel in python


#  tupel is immutable  and all most same of list

tup = (1,)

my_tupel = (1,2,3,4,5,6,7,7,7,7,7,8,9)

print(my_tupel[0:5])



# tupel methods





print(my_tupel.count(7))

print(my_tupel.index(7))



# practice 

'''movie1 = input("Enter 1 st favorite movie : ")
movie2= input("Enter 2 st favorite movie : ")
movie3 = input("Enter 3 st favorite movie : ")

list = []

list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)'''


'''li = [1,2,3,2,1]

li_cop = li.copy()

li_cop.reverse()

if li_cop == li :
    print(" this list is pelindrome : ")
else :
    print(" this list is  not pelindrome : ")'''


# l = [15,2,4,36,2,514,25,36,69,68,57]
# n_l = [ i  for i in l if i>21]

# print(n_l)  this called list comprihensivef


n = int(input("size of list : "))
 

ls = []

for i in range(n):
    num = int(input())
    ls.append(num)

idx1 = int(input("enter index 1 : "))
idx2 = int(input("enter index 2 : "))

t_l = ls[idx1]
ls[idx1] = ls[idx2]
ls[idx2] = t_l

print(ls)

