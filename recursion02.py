#recursion
#why it need: we breeakdown larger problem into smaller problem it solve repitadly 
#when use : scenario case
"""
one large list contain another list and it will contain lot of elements a folder contain another large folder 
that timings use recursion it will be solve repitadly by itself
"""
#sum of list number use recursion
# a=[2,[3,8],[3,[4,5,6,7]],[3,5,7,8,11]]
def real_values(a):
    total=0
    for values in a:
        if isinstance(values,list):
            total=total+real_values(values)
        else:
            total=total+values
    return total

print(real_values([2,[3,8],[3,[4,5,6,7]],[3,5,7,8,11]]))

#flow
"""
1.first we define the function and call li based on the arguments
2.after it will enter or start execute the program
3.enter loop check the condition and isinstance means -the given arguments is list or not
otherwise check it print else parts
"""