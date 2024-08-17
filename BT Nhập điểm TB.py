# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:37:13 2024

@author: NGUYỄN ĐỨC HUY - 23730841

"""
distance = float(input("Nhập điểm trung bình (GPA):"))

if distance < 3.5:
    print("Học lực kém")
elif distance >= 3.5 and distance < 5.0:
    print("Học Lực Yếu")
elif distance >= 5.0 and distance < 7.0:
    print("Học lực Trung bình")
elif distance >= 7.0 and distance < 8.0:
    print("Học Lực Khá")
elif distance >= 8.0 and distance < 9.0:
    print("Học lực Giỏi")
elif distance >= 9.0 and distance <= 10:
    print("Học lực Xuất sắc")
else:
    print("Điểm GPA không hợp lệ")