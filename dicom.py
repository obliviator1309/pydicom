# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:03:49 2019

@author: user
"""

import pydicom
from pydicom.tag import Tag
ds = pydicom.dcmread("ttfm.dcm")
ds1 = pydicom.dcmread("bmode.dcm")
#print(ds)
#print(ds1)
#print(ds[0x0028,0x0002].value)
#print(ds[0x7fe0,0x0010].value)
#t1 = Tag(0x0028,0x0011)
#print(t1)
file = open("output.txt", "a+")
file.write(str(ds))
file.close()

file1 = open("output1.txt", "a+")
file1.write(str(ds1))
file1.close()