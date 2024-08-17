# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:46 2024

@author: Nguyễn Đức Huy - 23730841
"""

from random import randint
nguoi = int(input("Ban vui long chon: 1.Keo, 2.Bua, 3.Bao : "))
may = randint(1,3)
if may == 1:
    print("May chon Keo")
if may == 2:
    print("May chon Bua")
if may == 3:
    print("May chon Bao")
if may == nguoi:
    print("Hoa")
if may == 1 and nguoi == 2:
    print("Thang")
if may == 1 and nguoi == 3:
    print("Thua")
if may == 2 and nguoi == 3:
    print("Thang")
if may == 2 and nguoi == 1:
    print("Thua")
if may == 3 and nguoi == 1:
    print("Thang")
if may == 3 and nguoi == 2:
    print("Thua")

