#map 
#it is in built function in python it will change every number or values in iterable
a=[5,4,5,8,3]
result=map(lambda x:x*2,a)
print(set(result))    #it will convert list into set

#filter
#it is also in built function in python 
# it will filter or mainly work on the specfic item 
list=[2,5,6,4,9,7]
result=filter(lambda x:x%2==0,list)
print(tuple(result))

#sorted
#it is buit in function in python 
#it will sort the number of values (ascending or descending order) based on the condition
#it will sort the numbers in given iterable number only
num=[2,8,9,4,2,7]
result=sorted(num,key=lambda x :x*2,reverse=True)
print(result)  #it will sort the numbers in given iterable values
