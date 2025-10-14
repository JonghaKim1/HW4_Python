from typing import Final

def my_steps(n: int) -> int:
    """
    Return the number of distinct ways to climb a ladder of n steps when only able to move 1 or 2 steps.
    1<= n <= 25
    ValueError: if n is outside the valid range.
    """

    if not isinstance(n, int) or n < 1 or n > 25:
            raise ValueError("n must be an integer between 1 and 25 inclusive")
    
    #Base cases: f(1)=1, f(2)=2
    if n == 1:
          return 1
    if n == 2:
          return 2
    
    #Iterative Fibonnaci-style sequence
    prev2: Final[int] = 1 # f(1)
    prev1: Final[int] = 2 # f(2)
    a, b = prev2, prev1

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b