# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class employee():
    
    numberofemployees=0
    raise_amount=1.5
    def __init__(self,first,last,pay):
        self.first=first #first name
        self.last=last #last name
        self.pay=pay #salary/pay
        self.email=first+'.'+last+'@company.com' #email using first and last name and adding @company.com
        employee.numberofemployees+=1 #number of empployees will be incremented by 1 everytime a niew instance of the class is created
        

    def fullname(self):
        #print ('{} {}'.format(self.first,self.last))
        return self.first+' '+self.last #reutrn the full name
        
    def apply_raise(self):
        self.pay=self.pay*self.raise_amount
        return self.pay #returns their pay after increment
        
    @classmethod #alternative constructor to parse strings having _ and then passing the same to create an instance of employee class
    def parse_string(cls,emp_str):
        first,last,pay=emp_str.split('_') #parsing the values from the string
        return cls(first,last,pay) 
    
    
        



      
        
        
    


