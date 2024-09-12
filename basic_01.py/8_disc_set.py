#   dictionary are use to store data values in key:values pair 
# dict is mutable & dont allos dublicate key & allow all data type 

# My_Info = {
      
#     "name" : "chirag",
#     "age"  : 17 ,
#     "study": "diploma is Runing..",
#     "subjec":{
#          "py": 9.9,
#          'eng':3.5
#      }

# }

# emety_dict = {}

# print(My_Info["name"])
# My_Info["name"]="jikadra chirag"
# My_Info
# print(My_Info)




# # dict methods

# print((list(My_Info.keys()))) # get all dict key help of keys method

# print(list(My_Info.values()))

# print(list(My_Info.items()))

# print((My_Info.get("name")))

# print((My_Info.update({"city":"surat"})))

# print(My_Info)



# ############# set in python   se is muteble
# # unodered & unique items are store &  set elimen is immutable
# # ignore dublicate values

# set1 = set()
# set = {1,2,3,4,5,6,"chirag",7,8,9}
# print(len(set))
# print(type(set))

# set.add("jikdra")

# set.discard("any")

# set.remove("jikdra")

# set.pop()
# set2 ={1,2.3,4,5,6,99,78,"chirag","prajapati",1,2,0,15,0,5,5,0}
# # set.clear()
# set.union(set2)
# print(set2.union(set))
# print(set.intersection(set2))
# set.intersection_update(set2)
# set.symmetric_difference_update(set2)
# print(set)
# for i in set :
#     print (i)



# practice

li = [1,2,5,8,6,7,4,5,8,5]
li2 = [9,8,5,]
li3 = [8,1,5,55,5,55,55]

s1 = set(li)
s2 = set(li2)
s3 = set(li3)

ds = s1.intersection(s2)
print(ds)
ds.intersection(s3)
f_l =list(ds)
print(f_l)


input_sring = input("enter a sring : ")
n = int(input("enter n : "))
alphabets = "abcdefghijklmnopquvxyz"
reversed_alpha = alphabets[::-1]
dict1 = dict(zip(alphabets,reversed_alpha))


prefix = input_sring[0:n-1]
suffix  = input_sring[n-1:]


mirror = ""

for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]


res = prefix + mirror
print(res)








