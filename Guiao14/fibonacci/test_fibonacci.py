# test_fibonacci.py
import pytest
from fibonacci import fibonacci

def test_no_arguments():
    assert fibonacci() == 'ERROR: Argument missing' 

def test_inferior_1():
    print("Testa comportamento com n < 1")
    assert fibonacci(0) == [0]
    assert fibonacci(-1) == []

def test_igual_1(): 
    assert fibonacci(1) == [0 , 1]

def test_igual_2():
    assert fibonacci(2) == [0 , 1 , 1]

def test_igual_5():
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    
def test_maior_2():
    import random 
    n = random.randint(1, 1000)
    r = fibonacci(n)
    
    assert len(r) ==  n + 1


