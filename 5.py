base = 1600

def electricPay(kwh):
    if(kwh<100):
       return kwh*60.7 +410
    elif(kwh<=200):
        return 100*60.7+(kwh-100)*125.9 +910
    elif(kwh>200):
        return 100*60.7+100*125.9+(kwh-200)*187.9+1600
        
kwh=int(input('전기값입력: khw: '))        
result= (electricPay(kwh)%0.037)+(electricPay(kwh)%0.1)+electricPay(kwh)
print (f'{int(result)}원 입니다.')