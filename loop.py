#Looping the list 
n = int(input("length of the list:-"))
list1 = []
for i in range(n):
    element = input("enter the element:-")
    list1.append(element)

print("list elements are:-",list1)