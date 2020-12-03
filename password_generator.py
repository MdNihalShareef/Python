import random
def passgen():
    a=int(input("Enter the length of password "))
    c=int(input("Enter the no. of alphabets "))
    b=int(input("Enter the no. of digits "))
    d=int(input("Enter the no. of symbols "))
    s=["!","@","#","$","%","^","&","*","(",")",";",":","'",'"','<',",",".",">","?","/"]
    if a>=6 and b+c+d==a:
        p=[]
        for i in range(d):
            p.append(random.choice(s))
        for i in range(b):
            p.append(str(random.randint(0,9)))
        for i in range(c):
            g=random.randint(1,2)
            if g==1:
                p.append(chr(random.randint(65,90)))
            else:
                p.append(chr(random.randint(97,122)))
        random.shuffle(p)
        print("Password =","".join(p))
    else:
        if a<6:
            print("length of password is too small")
        if a!=b+c+d:
            print("Enter details in a correct manner")
        passgen()
passgen()