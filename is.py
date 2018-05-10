Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str="this is a python class"
>>> print str.isalpha()
False
>>> str="thisisapythonclass"
>>> print str.isalpha()
True
>>> 4
4
>>> 
>>> 
>>> str1='1234'
>>> str2="this is python"
>>> print isdigit()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print isdigit()
NameError: name 'isdigit' is not defined
>>> print str1.isdigit()
True
>>> print str2.isdigit()
False
>>> 
>>> 
>>> str3="this is python"
>>> str4="This is python"
>>> str5="this Is python"
>>> print str3.islower()
True
>>> print str4.islower()
False
>>> print str5.islower()
False
>>> 
>>> 
>>> 
>>> 
>>> str6="           p           "
>>> str7="                       "
>>> print str6.isspace()
False
>>> print str7.isspace()
True
>>> 
>>> 
>>> 
>>> str8="This Is Python"
>>> str9="this is Python"
>>> print str8.istitle()
True
>>> print str9.istitle()
False
>>> 
>>> 
>>> 
>>> str10="THIS IS PYTHON"
>>> print str10.supper()

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print str10.supper()
AttributeError: 'str' object has no attribute 'supper'
>>> print str10.isupper()
True
>>> 
>>> 
>>> str11="
SyntaxError: EOL while scanning string literal
>>> str11="_"
>>> str12=("a","b","c")
>>> printstr11.join(str12)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    printstr11.join(str12)
NameError: name 'printstr11' is not defined
>>> print str11.join(str12)
a_b_c
>>> print str12.join(str12)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print str12.join(str12)
AttributeError: 'tuple' object has no attribute 'join'
>>> print str12.join(str11)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print str12.join(str11)
AttributeError: 'tuple' object has no attribute 'join'
>>> print str11.join(str12)
a_b_c
>>> 
>>> 
>>> 
>>> ljust(width[,fillchar])
SyntaxError: invalid syntax
>>> ob="python"
>>> print ob.ljust(40,'$')
python$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
>>> print ob.ljust(40,'')

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print ob.ljust(40,'')
TypeError: ljust() argument 2 must be char, not str
>>> print ob.ljust(40,' ')
python                                  
>>> print ob.rjust(40,' ')
                                  python
>>> 
>>> 
>>> 
>>> str13="this is python"
>>> print len(str)
18
>>> print len(str13)
14
>>> str14="         python"
>>> print str14.istrip()

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print str14.istrip()
AttributeError: 'str' object has no attribute 'istrip'
>>> print str14.lstrip()
python
>>> print str14.lstrip(" ")
python
>>> print str14.lstrip("n")
         python
>>> print str13.lstrip()
this is python
>>> print str13.lstrip("t")
his is python
>>> print str13.lstrip("h")
this is python
>>> 
>>> 
>>> 
>>> str="this is a python class. It is very boring"
>>> print str.replace("is","was")
thwas was a python class. It was very boring
>>> print str.replace(" is","was")
thiswas a python class. Itwas very boring
>>> print str.replace("  is","was")
this is a python class. It is very boring
>>> str="this is a python class. It is very boring"
>>> print str.replace("  is","was")
this is a python class. It is very boring
>>> print str.replace(" is","was")
thiswas a python class. Itwas very boring
>>> print str.replace("  is"," was")
this is a python class. It is very boring
>>> str="this is a python class. It is very boring"
>>> print str.replace("  is"," was")
this is a python class. It is very boring
>>> print str.replace(" is"," was")
this was a python class. It was very boring
>>> 
>>> 
>>> 
>>> 
>>> www.rogramiz.com/python-programming/quiz/decision-making/take/
SyntaxError: invalid syntax
>>> 
>>> 
