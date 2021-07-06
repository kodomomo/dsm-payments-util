from random_words import word_list
import random

s_chars = ['!', '@', '#', '*', '?']


def generate_random_password():
    return f'{random.choice(word_list).lower()}-{random.choice(word_list).lower()}{random.choice(s_chars)}'




print("test gen random pw :",generate_random_password())
