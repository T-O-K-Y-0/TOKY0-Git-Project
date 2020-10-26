from random import randint as rand
from os import system as sys

chars = "+-/*!&$#?=@<>abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890"

lenght = int (input( "Passwords lenght: " ))
password = ''

for i in range( lenght ):
	password = f'{password}{chars[rand(0, len(chars)-1)]}'

input( password )