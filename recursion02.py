#recursion
#why it need: we breeakdown larger problem into smaller problem it solve repitadly 
#when use : scenario case
"""
one large list contain another list and it will contain lot of elements and  a folder contain another large folder 
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
1.first it will define and again move tocall the function
2.again it will assign the values based on condition nxt move to loops
3.check the condition isinstance -means it check is list or not given calling values and again 
and again it will do untill the condition false.
"""