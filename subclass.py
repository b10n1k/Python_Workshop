#!/usr/bin/env python
#Filename:subclass.py

from Person import Person

class Me(Person):
    '''This class inherits form Person Class'''

    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age=age

    

