#!/usr/bin/env python
#Filename: Person.py

class Person:
    """This is the super class of Person"""

    def __init__(self, name=""):
        """constructor"""
        self.name=name
        self.introduce()
        print ">>>>"
        self.check_empty_name()
    #import more details

    def introduce(self):
        """print a msg"""
        print "My name is ", self.name
        
    def check_empty_name(self):
        if self.name=="":
            instr=raw_input("Your name: ")
            self.name=instr
        else:
            pass
#p=Person()
#p.check_empty_name()
#p.introduce()
    #define extra methods
