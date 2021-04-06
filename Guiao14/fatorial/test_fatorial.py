import pytest

from fatorial import fatorial

def test_negativos():
 assert fatorial(-1) == "invalid"

def test_zero():
 assert fatorial(0) == 1

def test_valor_pequeno():
 assert fatorial(5) == 120

def test_valor_invalido():
 assert fatorial(None) == "invalid"
 assert fatorial("batatinhas") == "invalid"
 
