# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:46 2024

@author: Nguyễn Đức Huy - 23730841
"""

from random import randint
nguoi = int(input("Bạn hãy chọn ngẫu nhiên: 1.Kéo, 2.Búa, 3.Bao : "))
may = randint(1,3)
if may == 1:
    print("Máy chọn Kéo")
if may == 2:
    print("May chọn Búa")
if may == 3:
    print("Máy chọn Bao")
if may == nguoi:
    print("___Hòa___")
if may == 1 and nguoi == 2:
    print("Thắng")
if may == 1 and nguoi == 3:
    print("Thua")
if may == 2 and nguoi == 3:
    print("Thắng")
if may == 2 and nguoi == 1:
    print("Thua")
if may == 3 and nguoi == 1:
    print("Thắng")
if may == 3 and nguoi == 2:
    print("Thua")

