Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,35,78,60,80,75]
print(l.max(l))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(l.max(l))
AttributeError: 'list' object has no attribute 'max'
print(max(l))
80
print(min(l))
1
l=1,4,5,6,7,2,4,6,8,2]
SyntaxError: unmatched ']'
l=[1,4,5,6,7,2,4,6,8,2]
print(l.count(2))
2
print(l.count(4))
2
print(l.count(1))
1
print(l.count(0))
0
print(l.index(7))
4
#copied with same location
l2=l
print(l2)
[1, 4, 5, 6, 7, 2, 4, 6, 8, 2]
print(l)
[1, 4, 5, 6, 7, 2, 4, 6, 8, 2]
l2[0]=10
print(l2)
[10, 4, 5, 6, 7, 2, 4, 6, 8, 2]
print(l)
[10, 4, 5, 6, 7, 2, 4, 6, 8, 2]
#copied with differnt location
l2=l.copy()
print(l2)
[10, 4, 5, 6, 7, 2, 4, 6, 8, 2]
print(l)
[10, 4, 5, 6, 7, 2, 4, 6, 8, 2]
l2[1]=20
print(l2)
[10, 20, 5, 6, 7, 2, 4, 6, 8, 2]
print(l)
[10, 4, 5, 6, 7, 2, 4, 6, 8, 2]
#access
;=[1,2,3,4,5,6]
SyntaxError: invalid syntax
l=[1,2,3,4,5,6]
print(l)
[1, 2, 3, 4, 5, 6]
print(l[-1])
6
print(l[1:3])
[2, 3]
print(l[-1:-4])
[]
print(l[-4:-1])
[3, 4, 5]
print([-4:])
SyntaxError: invalid syntax
print([-4:])
SyntaxError: invalid syntax
print(l[1:4])
[2, 3, 4]
len(l)
6
