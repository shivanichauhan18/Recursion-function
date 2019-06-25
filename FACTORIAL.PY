def factorial(n):
    if n==1:
        return 1
    else:
        count=factorial(n-1)*n
        return count
print factorial(7)