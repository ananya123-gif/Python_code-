# Hexadecimal to Decimal Conversion
# Hexadecimal Number = 2545
# Decimal Number = 9F1

def hexa_to_dec(num):
    c=''
    while(num!=0):
        r=num%16
        if(r==10):
            c+='A'
        elif(r==11):
            c+='B'
        elif(r==12):
            c+='C'
        elif(r==13):
            c+='D'
        elif(r==14):
            c+='E'
        elif(r==15):
            c+='F'
        else:
            c+=str(r)
        num=num//16

    print(c[::-1])

num=int(input())
hexa_to_dec(num)
