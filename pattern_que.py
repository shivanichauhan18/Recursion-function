def twopowers(number):
    if number==1:
        return 1
    return 2 * twopowers(number-1)

index=1
while(index<10):
    print(twopowers(index))
    index+=1
print " "

def pattern(n):
    if n==1:
        return 1
    return (pattern (n-1) +3)
print pattern(5)