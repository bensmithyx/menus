# Menus
Easy CLI menu creation tool

# Installation
`pip install python-menu`

# Menu Example
```py
>>> from menu import *
>>>  menu1 = Menu(title="Menu1",options=["option1","option2","option3"], result="index"
>>> menu1.show()
[+] Menu1        [1] option1     [2] option2     [3] option3

(Menu) > 1
>>> print(menu1.value)
1
>>> menu1.update(title="Updated Menu1",options=["option1","option2","option3"], result="value")
>>> menu1.show()
[+] Updated Menu1        [1] option1     [2] option2     [3] option3

(Menu) > 1
>>> print(menu1.value)
option1
```
# Menu Example
```py
>>> from menu import *
>>> list1 = List(title="List1", options="Option 1",result="index")
>>> list1.show()
[+] 1 - Option 1

(Option) > 1
>>> print(list1.value)
1
>>> list1.update(title="Update List1", options=["Option 1","Option 2"],result="value")
>>> list1.show()
[+] 1 - Option 1

[+] 2 - Option 2

(Option) > 2
>>> print(list1.value)
Option 2
```
