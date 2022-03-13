# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:28:38 2022

@author: Vinod
"""

class  Person(object):  
    def  getGender(  self  ):  
        return  "Unknown"  
class  Male(  Person  ):  
    def  getGender(  self  ):  
        return  "Male"  
class  Female(  Person  ):  
    def  getGender(  self  ):  
        return  "Female"  
# Test
a_male  =  Male()  
a_female=  Female()  
print(a_male.getGender())  
print  (a_female.getGender())