def reverse_list(a):
    n=len(a)
    for i in range(n//2):
        a[i],a[n-i-1]=a[a-i-1],a[i]
    return list(a) 
        

# print ('몇개의 수를 입력하고 싶나요?')
d=[]
num = int(input('몇개의 숫자를 입력하고 싶나요?'))  
for i in range(0,num):
    d.append( int(input(f'{i} 째 수를 입력해주세요')))  
    
print (f'결과값: {reverse_list(d)}')
