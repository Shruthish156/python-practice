#SETS
#it is a unordered collection of elements
#it is mutable (we can modify,add,delete) and does not allow duplicate elemenmts
#already exists
#not allow indexing bcz it is unorderd
# it is denoted as :{}
num={1,2,3,4,1,3,8}
print(type(num))
print(len(num))      #5 because not allow repeated elements(1,3)
#methods 
num.add(56)          #add
print(num)  
num.remove(1)       #it print(2,3,4,8,56) not allow duplicate elements
print(num)
num.clear()
print(num)
#sets operation(intersection:&,union:|,difference:-)
#union:it is combing the both sets
set1={1,2,3,5,6}
set2={5,1,4,8}
print(set1 | set2)      #| this is union symbol in python
#intersection: it give common elements in both sets
print(set1 & set2)      #& it is symbol of intersection in python   print (1,5)
#difference : it give except common elements but give first which one label
print(set1 - set2)      # 2,3,6
print(set2- set1)       # 4,8

print()
#DICTIONARY
#it is mutable (weccan modify,add,remove)
#it is ordered collection of elements
#it is key value pair
#doesnot allow dupliocate keys but allow value
#allow indexing
student_name={
    "shruthisha":20,
    "sumantha":17,
    "ramu":52,
    "shruthisha":20,
    "raju":13

}
print(type(student_name))
print(len(student_name))       #4 bcz does not allow duplicate keys 
print(student_name["ramu"])    #52
#dictionary methods
#add
student_name["shruthi"]=56     
print(student_name)
#remove
#inn dictonary any removing use del,and pop 
del student_name["raju"]      #remove use del in class dict
print(student_name)
#modification
student_name["shruthisha"]=25
print(student_name)
print(student_name.keys())    #only print keys
print(student_name.values())  #only print values
print(student_name.items())   #it print whole dictionary
#nested dictionary
#it contain another dictionary
#1.dictionary to dictionary
student_marks={
    "ramu":{
        "shruthisha":20,
        "summu":17
    },
    "shruthisha":{
        "shruthisha":20,
        "summu":17
    }
}
print(len(student_marks))    #2 bcz it has a two keys are there
print(student_marks["ramu"]["shruthisha"])
#add
student_marks["shruthisha"]["shruthi"]=21
print(student_marks)
#modification
student_marks["ramu"]["summu"]=18
print(student_marks)
#dictionary to list to dictionary
student_marks={
    "ramu":[20],
    "subjects":{
        "kannada":95,
        "english":94,
        "hindi":20
    }
}
print(len(student_marks))
print(student_marks["ramu"])
student_marks["Ramu"]=[52]
print(student_marks)
print(student_marks)
print(len(student_marks))

