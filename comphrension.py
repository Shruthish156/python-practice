print("=======comphrensions=======")
#list comphrension 
#we write code logic use list within one line
#it is reduce the line of code
#smart,and efficient code
#easy to remember, variable=[condition for item in iterable]==list compherension 
list1=[2,8,9,7,5,46,3]
result=[x*x for x in list1]    #square of the each elements in list
print(result)
list=[]
for values in list1:
    if values%2==0:
        list.append(values)
print(list)
odd_num=[x for x in list1 if x%2 !=0 ]
print(odd_num)
#list comphrension using condition
list2=[5,7,6,8,9]
result=[x**2 for x in list2 if x%2==0]
print(result)

names=["shruthisha","summu","ramu","raju"]
result=[name for name in names if name.startswith("s")]    #only print start from s
print(result)
#use if else condition
values=[4,6,5,8,7,12,10,22]
result=[x**2 for x in values if x%2==0 and x<=8]         #it will print only even number from 0 to leess than or equal to 8
print(result)
out_put=["pass" if num>=45 else "odd" for num in range(30,50)]
print(out_put)

#dictionary comphrension
#syntax ={key_expr: value_expr for item in iterable}
student_names={"shruthisha","ramu","summu","raju"}
student_marks={50,55,85,56}

student_output={index:values for index,values in enumerate(student_names)}
print(student_output)
result={names:names*2  for names in student_names if len(names)>8}
print(result)



