Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=(5,6,8.9,2)
raj=("chicken","dark","mutton","icecream")
n=() #EMPTY TUPLE
r=("kitkat")
print(s)
(5, 6, 8.9, 2)
print(raj)
('chicken', 'dark', 'mutton', 'icecream')
print(n)
()
print(r)
kitkat
print(type(r))
<class 'str'>
print(type(raj))
<class 'tuple'>

#for singl valued tuple we have to put comma ,
dp=("munch")
print(type(dp))
<class 'str'>
dp=("beans",)
print(type(dp))
<class 'tuple'>

print("ACCESING TUPLE ELEMENTS")
ACCESING TUPLE ELEMENTS
raj[0]
'chicken'
print(n[0])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(n[0])
IndexError: tuple index out of range
n[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    n[0]
IndexError: tuple index out of range
r[0]
'k'
dp[0]
'beans'
#slicing
s[ :len(s)]
(5, 6, 8.9, 2)
s[1:4]
(6, 8.9, 2)
raj[-3]
'dark'
raj[-3:-1] #print -3 index val and -2 index val
('dark', 'mutton')
('dark', 'mutton')
('dark', 'mutton')
print("tuple concatination")
tuple concatination
print(s+raj)
(5, 6, 8.9, 2, 'chicken', 'dark', 'mutton', 'icecream')
del s[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    del s[0]
TypeError: 'tuple' object doesn't support item deletion

#reputation
print(dp*3)
('beans', 'beans', 'beans')
cmp(s,raj)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    cmp(s,raj)
NameError: name 'cmp' is not defined
print(cmp(raj,dp))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(cmp(raj,dp))
NameError: name 'cmp' is not defined
list(s)
[5, 6, 8.9, 2]
x=[3,"homa",8.1,"madhu"]
del s[1]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    del s[1]
TypeError: 'tuple' object doesn't support item deletion
print(s)
(5, 6, 8.9, 2)
e=list(s)
print(e)
[5, 6, 8.9, 2]
e[2]=7

print(e)
[5, 6, 7, 2]
print(s)
(5, 6, 8.9, 2)
print(list(s))
[5, 6, 8.9, 2]

min(s)
2
max(s)
8.9

max(raj)
'mutton'
print(raj)
('chicken', 'dark', 'mutton', 'icecream')
min(raj)
'chicken'
'chicken'
'chicken'
cmp(raj,dp)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    cmp(raj,dp)
NameError: name 'cmp' is not defined
s(x)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s(x)
TypeError: 'tuple' object is not callable
del s
print(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(s)
NameError: name 's' is not defined
