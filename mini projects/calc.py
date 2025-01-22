no1= float(input('1: '))
no2= float(input('2: '))
opr= input('op: ')
result= None

if opr == '+':
    result= no1 + no2

elif opr == '-':
    result= no1-no2


elif opr == '%':
    result= no1%no2


elif opr == '*':
    result= no1*no2


elif opr == '/':
    if no2 !=0 :
      result= no1/no2

    else:
        print("error")

if result is not None:
    print(result)
