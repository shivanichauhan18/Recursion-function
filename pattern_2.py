def pattern_no(n):
    if n<2:
    	sum=1
        return 1
    elif n%2==0:
        count = pattern_no(n-1)+3
        print count
        return count
    else:
        count1=pattern_no(n-1)*2
        print count1
        return count1
pattern_no(7)