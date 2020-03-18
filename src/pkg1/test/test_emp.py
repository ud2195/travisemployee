#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:50:02 2020

@author: espm1854
"""

import pytest
from pkg1.employee import employee

def test_on_fullname():
    employee1=employee('aaradhya', 'gupta', 10000)
    fullname=employee1.fullname()
    assert fullname=='aaradhya gupta','test passed'
    
    
def test_on_applyraise():
    employee2=employee('vijay','kapoor',50000)
    raiseamount=employee2.apply_raise()
    assert raiseamount==75000,'test passed'
