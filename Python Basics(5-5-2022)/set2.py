Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3}
s1={3,4,5}
print(s.difference(s2))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(s.difference(s2))
NameError: name 's2' is not defined. Did you mean: 's'?
print(s.difference(s1))
{1, 2}
print(s)
{1, 2, 3}
print(s1)
{3, 4, 5}
print(s.update(4,5,6))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(s.update(4,5,6))
TypeError: 'int' object is not iterable
print(s.update((4,5,6))
      print(s)
      
SyntaxError: '(' was never closed
s.update((4,5,6))
      
print(s)
      
{1, 2, 3, 4, 5, 6}
print(s.update(4,5,6))
      
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(s.update(4,5,6))
TypeError: 'int' object is not iterable
s.update(4,5,6)
      
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.update(4,5,6)
TypeError: 'int' object is not iterable
s.update((4,5,6))
      
print(s)
      
{1, 2, 3, 4, 5, 6}
print(s.difference_update(s1))
      
None
print(s)
      
{1, 2, 6}
print(s1.update_difference(s))
      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(s1.update_difference(s))
AttributeError: 'set' object has no attribute 'update_difference'
print(s1.difference_update(s))
      
None
print(s1)
      
{3, 4, 5}
s1={1,2,3}
      
s2={4,5,6}
      
print(s1.difference_update(s2))
      
None
print(s1)
      
{1, 2, 3}
