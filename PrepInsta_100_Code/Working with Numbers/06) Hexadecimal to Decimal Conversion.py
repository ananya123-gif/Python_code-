# Hexadecimal to Decimal Conversion
# HexaDecimal Number = C9
# Decimal Number = 201

def hexa_to_dec(num):
    s=str(num)
    s=s[::-1]
    c=0
    for i in range(len(s)):
        if(s[i]=="A"):
            c+=10*pow(16,i)
        elif(s[i]=="B"):
            c+=11*pow(16,i)
        elif(s[i]=="C"):
            c+=12*pow(16,i)
        elif(s[i]=="D"):
            c+=13*pow(16,i)
        elif(s[i]=="E"):
            c+=14*pow(16,i)
        elif(s[i]=="F"):
            c+=15*pow(16,i)
        else:
            c+=int(s[i])*pow(16,i)
    print(c)

num=input()
hexa_to_dec(num)
