Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
type(d)
<class 'dict'>
d["name"]="tanuja"
print(d)
{'name': 'tanuja'}
d['rno']=516
print(d)
{'name': 'tanuja', 'rno': 516}
len(d)
2
d['rno']=412
print(d)
{'name': 'tanuja', 'rno': 412}
d['class']=2333
print(d)
{'name': 'tanuja', 'rno': 412, 'class': 2333}
d.popitem()
('class', 2333)
print(d)
{'name': 'tanuja', 'rno': 412}
del(d["name"])
print(d)
{'rno': 412}
d.pop("rmo")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d.pop("rmo")
KeyError: 'rmo'
d.pop('rno)
      
SyntaxError: unterminated string literal (detected at line 1)
d.pop("rno")
      
412
d=dict([1,2),(3,4),(5,6)])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
d=dict([(1,2),(3,4),(5,6)])
print(d)
{1: 2, 3: 4, 5: 6}
d.keys()
dict_keys([1, 3, 5])
d.values()
dict_values([2, 4, 6])
d.items()
dict_items([(1, 2), (3, 4), (5, 6)])
d.get(1)
2
d.get(5)
6
d.get(3)
4
d.get(4)
