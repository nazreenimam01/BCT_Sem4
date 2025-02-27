d={1:'ABC',2:'DEF',3:'GHI'}
dn=d.fromkeys(d,'ABC')
print("Using fromkeys function on given dictionary=",dn)
print("To get value at key 2:",d.get(2))
print("To get the keys:",d.keys())
print("To get the values:",d.values())
l=d.pop(2)
print("Using pop function:",d)
print("The value popped is",l)
d.popitem()
print("Using popitem function:",d)
d.update({4:'MNO'})
print("Using update function:",d)

d1={}
L=[5,6,7]
d2 = d1.fromkeys(L,'ABC')
print("Using fromkeys function on list:",d2)
d3={}
d3=d2.copy()
print("Using copy function:",d3)
d2.clear()
print("Using clear function:",d2)



