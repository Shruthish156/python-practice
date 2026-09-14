#dictionary creation in different types
#type1.list tuple method
num=[("shruthisha",20),("summu",17),("ramu",52)]
student_age=dict(num)
print(student_age)

#typ2 2.zip method it is combing the two list or what you label variable
list1=["shruthisha","summu","ramu","raju"]
list2=[20,25,41,14]
combine_dict=zip(list1,list2)       #it is combining two lists
dictionary=dict(combine_dict)
print(dictionary)

#Enumerate method
#it mainly use for index and value timings it give both
student_names=["shruthisha","ramu","raju","summu"]
marks_lists=[99,85,25,74]
for index,values in enumerate(student_names):     
    print(index,values)

marks_lists=[99,85,25,74]
for index,values in enumerate(marks_lists):
    if values>30:
        print(index,values)
    else:
        print("invalid")

#zip method
#it is combining the two lists or what you declare it
class_subjects=["kannada","english","hindi","social"]
class_marks=[99,89,75,88]
for class_subject,class_mark in zip(class_subjects,class_marks):
    if class_subject=="kannada" and class_mark>90:
        print(f"the corect subject is {class_subject} and correct marks is {class_mark}")
    elif class_mark>80 and class_mark<=88:
        print(f"the correct subject is {class_subject} and correct marks is {class_mark}")
    else:
        print("invalid subject and marks")

#string
#it is immutable (we cannot modify ,add,delete)
#it allow indexing 
name="aiengshruthisha"
print(type(name))
print(name[1:5:2])
#string methods
#upper()
print(name.upper())  #it will print all capital letter
#lower()
print(name.lower())  #it will print all small letter
#count
print(name.count("h"))
#capitalise
print(name.capitalize())   #only first letter will be capital letter
#replace
print(name.replace("aiengshruthisha","aiengineeringshruthisha"))