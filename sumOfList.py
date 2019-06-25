def sum_list(n):
    print n
    if len(n)==1:
        return n[0]
    else:
        count=sum_list(n[1:])+n[0]
        return count
print sum_list([2,4,10,15])