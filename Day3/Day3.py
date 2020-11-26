A={"Maharastra":"Mumbai",
   "Telangana":"Hyderabad",
   "Tamilnadu":"Chennai"}
B={"karnataka":"Bengaluru",
   "Bihar":"Patna",
   "Kerala":"Trivandrum"}
#Task1
A.update(B)
print(A)
#task2
del A['Maharastra']
print(A)
#task3
a = ["Ai","DL","powerbi"]
b = ["ML","CV","tableau"]
C =  dict(zip(a,b))
print(C)
#task4
D= {"1","2","3","4"}
print(len(D))
#task5
E= {"1","2","3","4"}
set = D.intersection(E)
print(set)