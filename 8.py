def pwd(root, pwd):
    result=root
    for i in range(pwd-1):
        result*=root
    return result

        
root=int(input('정수 root 값을 입력하세요: '))        
x=int(input('정수 x 값을 입력하세요: '))

print(f'루트는 {pwd(root,x)}')


        
