# Menus
Easy CLI menu creation tool

# Example
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
