def pattern_no(n):
    if n<2:
        return 10
    elif n%2!=0:
        return pattern_no(n-1)*10
    else:
        return pattern_no(n-1)+1
print pattern_no(7)