Title: Attribute access methods
Tags: python 
Author: Charles
Summary: Python Strings
Date: 2015-05-16


This blog post is about the magic methods related to attribute access in python. This knowledge is would help you learning advanced concepts such as properties, descriptor, slots etc. 
Here I when I classes I refer to new-style classes which are classes that inherit `object` in Python2 (either directly or indirectly) and All classes in Python3. 


##### __getattr__:

This method is called when accessing an un-defined attribute in an object. 
The attribute is searched in self instance object, type's class object and its entire inheritence chain before invoking the `__getattr__` method.
`__getattr__` and all attribute access methods like `__setattr__`,`__delattr__`,`__getattribute__` is effective even if one of the parent class implements these method.
if a class in inheritence chain has custom `__getattr__` (or anyone of the attribute access method) defined and you dont want this behaviour then you can revert to normal behaviour by overridding the method with the default behaviou

```
  class Test2(Test1):
  def __getattr__(self,name):
    object.__getattr__(self,name) 
```

##### __setattr__:

Unlike `__getattr__`, `__setattr__` is called on attribute assignment irrespective of whether the attribute is already defined or not.
Be cautious of using `__setattr__` because an assignment in `__setattr__` on `self` causes infinite recursion like shown below.
To avoid infinite recursion you should use `__dict__` based assignment. In `__dict__` based assignment you are not assigning to self but on `__dict__`. surprisingly `setattr` builtin function is not an alternative to `__dict__` based assignment and it using it would also cause infinite recursion.

```
class TestClass():
  def __setattr__(self,name,value):
    self.name = value ### This will cause infinite recursion
    self.__dict__ = {name:value} ### This will cause infinite recursion
    self.__dict__[name] = value ### this will not cause infinite recursion since this is an assignment on __dict__ and not on self i.e the object.
    setattr(self,name) =  value ### this will also cause infinite recursion
```

##### __delattr__:

This method is similar to `__setattr__` but called on attribute deletion. 


##### __getattribute__:

This method is available only in new style classes. This method is called on any attribute access irrespective of it being defined or un-defined.
This is the method that delegates the call to `__getattr__` on undefined attribute access. Hence if you override `__getattribute__` make sure you either explicitly call `__getattr__` or raise an AttributeError exception on undefined attribute access.