# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:48:34 2024

@author: NGUYỄN ĐỨC HUY - 23730841
"""


print("Giải phương trình bậc 1: ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm!")
else:
    x = -b/a
    print("Nghiệm của phương trình là:", x)
    
