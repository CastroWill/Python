def fibonacci(n):
    if n < 2:
        return n
    else:
        fibo = fibonacci(n-1) + fibonacci(n-2)
        return fibo
        
'''
import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (6, 21),
    (7, 28),
    (8, 36),
    (9, 45),
    (10, 55)
    ])

def test_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado
'''
