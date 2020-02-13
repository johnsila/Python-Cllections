#list
print("LIST")
#list is a collection which is ordered and changable
student=["mercy","john","kamau","abdi"]
print("all list=",student)#print entire list

print()
print()

print("******Indexing*****")
#indexing
print("indexing.",student[1])#print item on index 1
print("negative indexing.",student[-1])#print item from the right using negative indexing
print("range indexing 1",student[1:])#print from range index 1 to end of list
print("range indexing 2",student[1:3])#print from range index 1 to index 3
print("range indexing 3",student[-4:-1])#negative range from -4 to -1
print("range indexing 4",student[:3])#print the first 3 items of the list from the left

print()
print()

print("*********CHANGING ITEM IN LIST")
#change item in list
student[2]="ken"
print(student)#change the item in index 2 of the list to ken
student[0]="mary"
print(student)#change the item in index 0 to mary

print()
print()

print("***LIST LOOP******")
#loop through list
couty =["machakos","nairobi","mombasa"]
for counties in couty:#print item by item
    print("loop result",counties)

print()
print()

print("***CHECKING IF ITEM EXISTS(IN)******")
#check if item Exists
if "kitui" in couty:
    print("correct, item is in the list")#check if the defined item is in the list and return it if yes
else:
     print("no item found")


print()
print()

print("***CHECK IF ITEMS NOT EXIST******")
#not in
if "kitui" not in couty:
    print("correct, item is  not in the list")#check if the defined item is not in the list and return yes if not
else:
     print("item found")

print()
print()

print("***LENGTH******")
#list length
print("lenght of list is",len(couty))#coount items in the list

print()
print()

print("***ADD ITEM USING APPEND()******")
#add item to list using append
couty.append("kitui")#add kitui to the couty list
print(couty)

print()
print()

print("***ADD USING INDEX()******")
#add item to index 2 using insert method
couty.insert(2,"kisumu")
print(couty)

print()
print()

print("***JOIN LIST******")

#join 2 lists
a=['a','b','c']
b=['1','2','3']
list=a+b#join list a and b
print(list)


print()
print()

print("***REMOVE()******")
#remove item from list using remove()
fruits=["mangoes","orange","sugarcane","lemon"]
fruits.remove("lemon")#remove item lemon from the list
print(fruits)

print()
print()

print("***REMOVE USING POP******")
#remove specified index on the list using pop()
fruits.pop()#remove last item on the list
print(fruits)
fruits.pop(0)# removes specified item index on the list
print(fruits)

print()
print()

print("***DEL KEYWORD******")
#del keyword
integers=[1,2,2,4,5,6,7]
del integers[0]# deletes specified item on the list
print(integers)

del integers# delete the entire list

print()
print()

print("***CLEAR OPERATION******")
#clear()
veg=["mangoes","orange","sugarcane","lemon"]
veg.clear()#clears all items in the list
print(veg)

print()
print()

print("***COPY LIST******")
#copy a list. copy()
room=["p201","p202","p203","p200"]
rooms= room.copy()#make a copy of a list
print(rooms)

print()
print()

print("***REVERSE LIST******")
#reverse()
room.reverse()#rewrites the list from the right to the left
print(room)

print()
print()

print("***SORT()******")
cars = ['Ford', 'BMW', 'Volvo','mercedes','isuzu']
cars.sort()#sorts list using alphabetical order of the 1st character of the item
print(cars)
print("****SORT USING REVERSE****")
cars.sort(reverse=True)
print(cars)#Sorts item in decending order
print("*****SORT USING FUNCTION*****")
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars.sort(key=myFunc)#sorts item by counting the one with least chatasters to the most
print(cars)


