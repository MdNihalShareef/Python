a=[]
d=[]
b=0
def call():
    try:
        while 1:
            b=input("Enter number ")
            if b=='done':
                if len(d)!=0:
                    for i in d:
                        print(i,end=",")
                    print(" is/are not integers,so they are not taken in consideration")
                print("max =",max(a),'\nmin =',min(a))
                return
            elif type(int(b))==int:
                a.append(b)
    except:
        d.append(b)
        call()
call()