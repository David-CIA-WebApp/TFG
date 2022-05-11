import random
from encriptacion import *

def token_generator():
    with open("words.txt") as file:
        word = random.choice(file.read().split(" "))
        return encriptar(word, 32)

def encrypt_password(password):
        return encriptar(password, 64)
    
