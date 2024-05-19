import numpy as np

def extract_age(text):
    pos = int(text.index('-'))
    a = int(text[1:pos])
    b = int(text[pos+1:-1])
    return (a+b)//2


def my_sampling(mystring: str, highest: int, middle: int, lowest: int):
    if mystring == '<30':
        return True
    elif mystring == '>30':
        return np.random.choice([True, False], p=[lowest/middle, 1-lowest/middle])
    else:
        return np.random.choice([True, False], p=[lowest/highest, 1-lowest/highest])


