def first(n):
    divBool=False
    while(divBool==False):
        if(n%2!=0 or n%3!=0 or n%4!=0 or n%5!=0 or n%6!=0 or n%7!=0 or n%8!=0 or n%9!=0 or n%10!=0):
            n+=1
            divBool=False
        else:
            divBool=True
    return n

def second(n):
    divBool=False
    while(divBool==False):
        if(n%11!=0 or n%12!=0 or n%13!=0 or n%14!=0 or n%15!=0 or n%16!=0 or n%17!=0 or n%18!=0 or n%19!=0 or n%20!=0):
            n+=1
            divBool=False
        else:
            divBool=True
    return n


print(first(11) or second(21))
