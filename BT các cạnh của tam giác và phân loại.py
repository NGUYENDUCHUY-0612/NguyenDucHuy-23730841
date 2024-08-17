# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:03:03 2024

@author: Nguyễn Đức Huy - 23730841
"""
print("Nhập các cạnh để xác định đó có phải tam giác không")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c>a):

   if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
       print('Là Tam giác Vuông')
   
   elif a==b and b==c:
       print("Là Tam giác Đều ")
   
   elif a==b or a==c or b==c:
       print("là Tam giác cân")
       
   elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
       print("Là tam giác tù")

   else:
       print("Là tam giác nhọn")
   
 
