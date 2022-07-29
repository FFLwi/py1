def reverse_list(a):
    n=len(a)-1
    for i in range(n//2):
        a[i],a[n-i-1]=a[a-i-1],a[i]
    return list(a) 
i=0
d=list()
# s=int(input(f'{i} 째 수를 입력해주세요'))
while(1):
    s=input(f'{i} 째 수를 입력해주세요')
    d.append(s)
    if(d[i] =='n'):
      break

    i+=1
  
print ({reverse_list(d)})
# print (f'결과값: {reverse_list(d)}')