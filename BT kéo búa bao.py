# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:46 2024

@author: Nguyễn Đức Huy - 23730841
"""

import random

def get_computer_choice():
    """Hàm để máy tính chọn ngẫu nhiên kéo, búa, hoặc bao"""
    options = ["kéo", "búa", "bao"]
    return random.choice(options)

def get_user_choice():
    """Hàm để nhận lựa chọn từ người chơi"""
    choice = input("Nhập kéo, búa hoặc bao: ").strip().lower()
    while choice not in ["kéo", "búa", "bao"]:
        print("Lựa chọn không hợp lệ! Hãy nhập lại.")
        choice = input("Nhập kéo, búa hoặc bao: ").strip().lower()
    return choice

def determine_winner(user_choice, computer_choice):
    """Hàm để xác định người thắng cuộc"""
    if user_choice == computer_choice:
        return "Hòa!"
    elif (user_choice == "kéo" and computer_choice == "bao") or \
         (user_choice == "búa" and computer_choice == "kéo") or \
         (user_choice == "bao" and computer_choice == "búa"):
        return "Bạn thắng!"
    else:
        return "Máy thắng!"

def play_game():
    """Hàm chính để chạy trò chơi"""
    print("Chào mừng bạn đến với trò chơi Kéo, Búa, Bao!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Bạn chọn: {user_choice}")
    print(f"Máy chọn: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
