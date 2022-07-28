from re import A


print('a부터 b까지 정수의 합을 구합시다')
a=int(input('정수 a 값을 입력하세요'))
b=int(input('정수 b 값을 입력하세요'))

if a>b:
    a,b =b,A
    
sum=0
    
for i in range(a, b):
   
    print(f'{i}+', end='')
    sum+=i


print(f'{i}= ', end="")
sum += b
print (sum)