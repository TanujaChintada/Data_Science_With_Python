Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3)
print(t)
(1, 2, 3)
t[0]=10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[0]=10
TypeError: 'tuple' object does not support item assignment
x=list(t)
type(t)
<class 'tuple'>
type(x)
<class 'list'>
x[0]=888
print(x)
[888, 2, 3]
print(t)
(1, 2, 3)
t=tuple(x)
print(t)
(888, 2, 3)
s1={1,2,3}
print(s1)
{1, 2, 3}
s2={3,4,5}
print(s2)
{3, 4, 5}
type(s1)
<class 'set'>
help(s1)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

s1.union(s2)
{1, 2, 3, 4, 5}
s1.intersection(s2)
{3}
s1.difference(s2)
{1, 2}
s2.difference(s1)
{4, 5}
print((s1)
print(s1)
      
SyntaxError: '(' was never closed
print(s1)
      
{1, 2, 3}
s1.update({6,7,8})
      
print(s1)
      
{1, 2, 3, 6, 7, 8}
s1.difference_update(s2)
      
print(s1)
      
{1, 2, 6, 7, 8}
{1, 2, 6, 7, 8}
      
{1, 2, 6, 7, 8}
s={1,3,5}
      
print(s.add(7))
      
None
s.add(7)
      
print(s)
      
{1, 3, 5, 7}
x=set("hello world")
      
print(x)
      
{'r', 'o', 'e', 'd', 'h', ' ', 'l', 'w'}
x="tanuja"
      
x.pop()
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x.pop()
AttributeError: 'str' object has no attribute 'pop'
x={1,3,5,6}
      
x.pop()
      
1
print(x)
      
{3, 5, 6}
x.pop()
      
3
print(x)
      
{5, 6}
x.clear()
      
print(x)
      
set()
names={"tanu","adarsh","soumya"}
      
name2=names.copy()
      
print(name2)
      
{'adarsh', 'tanu', 'soumya'}
print(names)
      
{'adarsh', 'tanu', 'soumya'}
name2.add("chanti")
      
print(name2)
      
{'adarsh', 'chanti', 'tanu', 'soumya'}
name.remove("chanti")
      
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name.remove("chanti")
NameError: name 'name' is not defined. Did you mean: 'names'?
name2.remove("chanti")
      
print(name2)
      
{'adarsh', 'tanu', 'soumya'}
.clear
      
SyntaxError: invalid syntax
A={'a','b','c','d','e'}
      
B={'c','d','e'}
      
print(A.symmetric_differnce(B))
      
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(A.symmetric_differnce(B))
AttributeError: 'set' object has no attribute 'symmetric_differnce'. Did you mean: 'symmetric_difference'?
print(A.symmetric_difference(B))
      
{'b', 'a'}
c={}
      
print(A.symmetric_difference(B))
      
{'b', 'a'}
print(A.symmetric_difference(c))
      
{'a', 'c', 'b', 'e', 'd'}
print(B.symmetric_difference(c))
      
{'c', 'e', 'd'}
a={1,2,3,4,5}
      
b={1,2,3}
      
c={1,2,3}
      
print(a.superset(b))
      
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(a.superset(b))
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
print(a.issuperset(b))
      
True
print(b.issuperset(a))
      
False
print(c.issuperset(b))
      
True
print(b.issubset(a))
      
True
x={1,2,3,4}
      
y={5,6,7,8}
      
print(x.isdisjoint(y))
      
True
print(y.isdisjoint(x))
      
True
