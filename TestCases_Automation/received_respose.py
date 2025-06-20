"""
required only if what is received require translation
"""

def recursive_factorial(n: int) -> int:
    if n==0 or n==1:
        return 1
    return n*recursive_factorial(n-1)

if __name__ == '__main__':
    print(recursive_factorial(7))