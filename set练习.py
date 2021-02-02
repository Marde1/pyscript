# -*- coding:utf-8 -*-

s1 = {1,3,5,7,9}
s2 = {0,2,4,6,8}
s3 = {1,2,3,4,5,6}
s4 = {1,3,5,7,9,11,13,15}
print("s1是s2的子集：",s1.issubset(s2))
print("s1是s4的子集：",s4.issuperset(s1))
print("s1中不包含s3的集合元素：",s1.difference(s3))
print("s1和s2的并集：",s1.union(s2))
print("s1和s3的交集",s1.intersection(s3))
print("s2和s3的交集",s2.intersection(s3))

print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s3)
print(s1)