a=str(input('주유소 a, b 선택: '))
b=int(input('리터 선택'))
def price(a, b):
    if(a=='a'):
       return b*100
    elif(a=="b"):
        if(b<=50):
            return a*150
        elif(b>50):
            return a*75
print (f'안녕하세요{price(a,b)}')