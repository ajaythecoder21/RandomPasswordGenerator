# -*- coding: utf-8 -*-
print('Welcome to the PyPassword Generator!')
print('How many letters would you like in your password?')

letters = input('How many letters would you like in your password?')
symbols = input('How many symbols would you like?')
numbers = input('How many numbers would you like?')


import random
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
letter_list = ['a', 'b', 'c,' 'd', 'e', 'f', 'g', 'h','i', 'j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z']
password_list = []
for i in range(int(letters)):
    letter = random.choice(letter_list)
    #print(letter)
    password_list.append(letter)
    
symbol_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '\'', '?']
for i in range(int(symbols)):
    symbol = random.choice(symbol_list)
    #print(symbol)
    password_list.append(symbol)

numbers_list = ['0', '1', '2','3', '4','5', '6', '7', '8', '9']
for i in range(int(numbers)):
    number = random.choice(numbers_list)
    #print(number)
    password_list.append(number)
#print(password_list)
random.shuffle(password_list)

password = ''.join(password_list)

print('Your password is ' + password)
#password_list = random.shuffle(password_list)
#print(password_list)


