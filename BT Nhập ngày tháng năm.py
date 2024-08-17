# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:07:47 2024

@author: Nguyễn Đức Huy - 23730841
"""
print("Nhập ngày-tháng-năm, kiểm tra tính hợp lệ")
s = input("Nhap ngay, thang, nam (dd/mm/yyyy): ")

try:
    ngay, thang, nam = map(int, s.split("/"))
except ValueError:
    print("Dinh dang ngay khong hop le.")
else:
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        check = True
    else:
        check = False
    x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check:
        x[1] = 29
    if nam < 1:
        print("Nam khong hop le.")
    elif thang < 1 or thang > 12:
        print("Thang khong hop le.")
    elif ngay < 1 or ngay > x[thang -1]:
        print("Ngay khong hop le.")
    else:
        print("Ngay, thang, nam hop le.")