people=[
    {"name":"Harry", "house": "Gryffindor"},
    {"name":"Cho", "house": "Ravenclaw"},
    {"name":"Draco", "house": "Slytherin"}
]

'''def f(person):
    return person["name"]
'''
# here 'f' takes 'people' as its parameter.
# 'key' is a sort method optional paramete which is used to do custom sorting
# 'reverse=True' to sort in descending order
# By default sorting is done in ascending order
# All can be sorted except dict.
 
'''people.sort(key=f, reverse=True)'''

#func.=> lambda  parameter(i.e,input):return(i.e,output)
people.sort(key=lambda person:person["name"])
print(people)