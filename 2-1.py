def min_of(a):
    min=a[0]
    for i in range(1, len(a)):
        if a[i] < min:
            min =a[i]
    return min

t=(4,7,5.6,2,3.14,1)
    
print(f'답은?: {min_of(t)}')