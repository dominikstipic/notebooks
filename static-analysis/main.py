"""
   Module docstring misses
"""
from typing import TypeVar

T = TypeVar('T')

def multiply_float(x: float, y: float) -> float:
    """
      Multiplies the two float numbers
    """
    return x*y

def multiply(x: T, y: T) -> T:
    """
      Multiplies the two float numbers
    """
    return x*y


multiply(3.2, 7.2)
