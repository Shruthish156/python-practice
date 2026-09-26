# LIST
#it is a collection of orderd elements
#it is a muatble we can add ,modify etc ,allow duplicate elements
#denoted as :[]
number=[1,25,36,7]    #number(label) is stored in stack and values are stored in stack
print(type(number))
print(len(number))
#list indexing
print(number[0])      #1
print(number[1:3])    #25,36
print(number[3:0:-2]) #it will skip(step) one-one  .3=start ,0=stop,-2=step
print(number[1:])     #it will print all elements from index 1
print(number[:3])     #it will print all elements but skip index 3 elements like 7
#skipping
name="shruthisha"
print(name[::2])      #srtih : it will be skill one one index
#reverse 
print(name[::-1])
print(name[::-2])  
#LIST METHODS
#POP : it will remove the last index elements
names=["ramu",["raju"],"summu","shruthish"]
print(names[2])
names.pop()         #it will remove the last index elements like shruthish
print(names)
#APPEND: it will add the elements in last index
names.append("engshruthish")
print(names)
names[1].append("summu")
print(names)
print(len(names))   #it give four because it treatd as it add in same index of last elements
#INSERT: we insert the  elements in a specific index 
names.insert(1,"aishruthisha")
print(names)
#REMOVE :it will remove the elements based on the condition
names.remove("summu")
print(names)
#MODIFICATION : it will add the perticular elements in perticular index
names[2]="Ai shruthiha"
print(names)
value=[36,25,12,3,9,8]
value.sort(reverse=True)   #it is print from desecending order
print(value)      #it is method
b=sorted(value)   #it is a function create a new lists and original list remains unchanged
print(b)
print(value)
#EXTEND
a=[5,2,6,7,9]
a.extend([1,2,25,6])   #it will combine the list 
print(a)
a.reverse()            #it will be the reverse of whole list
print(a)

print()

#TUPLES
#it is a collection of the ordered elements 
#it is allow duplicate elements but it is immutable doesn't modify
#denoted as :()
n=(1,3,4,1)
n1=(1,3,5,6)
print(type(n))
print(len(n))
print(n+n1)    # tuple does not modify add ,remove but we can easy to add two tuples use operation(+)

print()
#SETS
#it is unrderd collection of elements
#it is mutable (we can modify and add and delete),but it is does not allow duplicate elements
#it is denoted as:{}
values={1,2,25,1,2,6}
print(values)
print(len(values))    #4 bcz does not allow repited values : 1,2
print(type(values))   #check data types but values treated as label store in stack and inside sets treated as values stored in stack

#conversion involving between list,typles,sets using the function
a=[1,25,3,4,1,3]
b=tuple(a)            #conversion of tuples
print(b)
c=set(a)  
print(c)
