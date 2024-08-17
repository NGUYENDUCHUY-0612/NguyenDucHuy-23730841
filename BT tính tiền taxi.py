# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:28:03 2024

@author: Nguyễn Đức Huy - 23730841
"""

#Tính tiền taxi theo số km quãng đường đi được:
a = float (input("Số km quãng đường đi được: "))
if a==1:
    print("Tổng tiền: ",20,"k")
elif a<=3:
    print("Tổng tiền: ", a*13,"k")
elif a<=8:
    print("Tổng tiền: ", 3*13+(a-3)*12,"k")
else:
    b = 3*13+5*12+(a-8)*10
    if b <= 100: 
        print("Tổng tiền: ", b,"k")
    else:
        print("Tổng tiền: ", b*0.92,"k")