s1={1,2,7,4,9,6}
s2={2,9,7}
print("s1=",s1)
print("s2=",s2)
print("Intersection of s1 and s2=",s1.intersection(s2))
print("Union of s1 and s2=",s1.union(s2)) 
print("Is s2 subset of s1?",s2.issubset(s1))
print("Is s1 superset of s2?",s1.issuperset(s2))
s1.pop()
print("After using pop function on s1:",s1)
s1.clear()
print("After clearing s1:",s1)
s3={1,2}
print("Intersection of s2 and s3=",s2.intersection(s3))
print("Union of s2 and s3=",s2.union(s3)) 
print("Is s3 subset of s2?",s3.issubset(s2))
print("Is s2 superset of s3?",s2.issuperset(s3))