m={}
print(type(m))
h=set()
print(type(h))
s={1,2,3,1,8,4,2,6,5,3,7}
print(s)
s.add(12)
print(s)
s.update([13,3,9,4],[2,8,6,17,20])
print(s)
s.discard(13)
print(s)
s.discard(22)
print(s)
s.remove(7)
print(s)
# s.remove(50)
# print(s)
# Error if item is not present in set
