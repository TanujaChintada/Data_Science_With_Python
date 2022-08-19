Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="tanuja"
print(a.upper())
TANUJA
a.upper())
SyntaxError: unmatched ')'
a.upper()
'TANUJA'
a.lower()
'tanuja'
print(a.lower())
tanuja
print(a.title())
Tanuja
print(a*3)
tanujatanujatanuja
print(a*5)
tanujatanujatanujatanujatanuja
#string membership test
'a' in "tanuja"
True
print('a' in "tanuja")
True
print('a' in "sowmi")
False
#enumerate()
str="tanuja"
A=list(enumerate(str))
print(A)
[(0, 't'), (1, 'a'), (2, 'n'), (3, 'u'), (4, 'j'), (5, 'a')]
X="adarsh"
X=list(enumerate(X))
print(X)
[(0, 'a'), (1, 'd'), (2, 'a'), (3, 'r'), (4, 's'), (5, 'h')]
y="amma"
z=list(enumerate(y))
print(z)
[(0, 'a'), (1, 'm'), (2, 'm'), (3, 'a')]
#count of string
str="adarsh"
print(len(str))
6
#isalnum()
x="tanuja"
print(x.isalnum())
True
x="tanuja123"
print(x.isalnum())
True
x="tanuja 123"
print(x.isalnum())
False
(#because space is there)
    #isalpha
str="tanuja"
SyntaxError: '(' was never closed
str="tanuja"
print(str.isalpha())
True
str="tanuja123"
print(str.isalpha())
False
str="adarsh tanuja"
print(str.isalpha())
False
#isdecimal
str="123345"
print(str.isdecimal())
True
str="132tanu"
print(str.isdecimal())
False
str="12 345"
print(str.isdecimal())
False
str="199999"
print(str.isdecimal())
True
#isdogot()
str="146789"
print(str.isdigit())
True
#isnumeric())
str='\u00BD"
SyntaxError: unterminated string literal (detected at line 1)
s="\u00BD"
print(s.isnumeric())
True
"123TANU"
'123TANU'
s="123TAN"
print(s.isnumeric())
False
a="\A00153"
print(s.isnumeric())
False
#isprintable()
str=" "
print(str.isprintable())
True
str=''
print(str.isprintable())
True
a="my n@me i$ t@nuj#"
print(a.isprintable())
True
x="$#%*&#@!()*[]":|?_+"
SyntaxError: unterminated string literal (detected at line 1)
str="n# n@%^me i* 90 *tanu"
print(str.isprintable())
True
str="1234566\0"
[romt(str.isprintable())
print(str.isprintable())\
 
SyntaxError: '[' was never closed
print(str.isprintable())
 
False
str="12345@&*/8910"
 
print(str.isprintable())
 
True
str=''
 
print(str.isprintable())
 
True
#isprintable
 
str="1 2 3 4"
 
print(str.isprintable())
 
True
print(str.isspace())
 
False
str=''
 
str=" "
 
print(str.ispace())
 
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(str.ispace())
AttributeError: 'str' object has no attribute 'ispace'. Did you mean: 'isspace'?
str="\n \n \n"
 
print(str.isspace())
 
True
str=" "
 
print(str.isspace())
 
True
str="\v \v \v"
 
print(str.isspace())
 
True
