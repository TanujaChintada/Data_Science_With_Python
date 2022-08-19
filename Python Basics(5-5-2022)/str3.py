Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="hfdshfuiaHRFIS"
print(a)
hfdshfuiaHRFIS
print(a.upper())
HFDSHFUIAHRFIS
print(a)
hfdshfuiaHRFIS
a="rajiv gandhi university"
print(a.capitalize())
Rajiv gandhi university
print(a.title())
Rajiv Gandhi University
print(a.upper())
RAJIV GANDHI UNIVERSITY
print(a.lower())
rajiv gandhi university
print(a.casefold())
rajiv gandhi university
a="banana"
print(a.center(20))
       banana       
print(a.center(50))
                      banana                      
print(a.center(100))
                                               banana                                               
print(a.center(10))
  banana  
x="tanuja name is tanuja"
print(x.count("tanuja"))
2
x="my name is tanuja"
print(x.encode())
b'my name is tanuja'
#concatenation
a="amma"
b="nanna"
s=a+b
print(s)
ammananna
a="tanuja'
SyntaxError: unterminated string literal (detected at line 1)
a="tanuja"
b="180516"
s=a+b
print(s)
tanuja180516
x=180516
y=a+x
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    y=a+x
TypeError: can only concatenate str (not "int") to str
x="ny name is tanuja"
print(x.endswith("a"))
True
print(endswith(.))
SyntaxError: invalid syntax
print(x.endswith(.))
SyntaxError: invalid syntax
print(x.endswith("."))
False
False
False
x="H\te\tl\tl\to
SyntaxError: unterminated string literal (detected at line 1)
x="H\te\tl\tl\to"
print(x.expandtabs(2))
H e l l o
print(x.expandtabs(5))
H    e    l    l    o

print(x.expandtabs(10))
H         e         l         l         o
s="hi how are you fine"
print(s.find("are"))
7
print(s.find("hi"))
0
print(s.find("you"))
11
print(s.find("fine"))
15


   
