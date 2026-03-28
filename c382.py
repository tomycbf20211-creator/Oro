a=input()
b=[]
c=['0','1','2','3','4','5','6','7','8','9']
y=""
for x in a:
    if x not in c:
        b.append(y)
        y=""
        b.append(x)
    else:
        y+=x
b.append(y)
if b[1]=='+':
    print(int(b[0])+int(b[2]))
elif b[1]=='-':
    print(int(b[0])-int(b[2]))
elif b[1]=='*':
    print(int(b[0])*int(b[2]))
else:
    print(int(b[0])//int(b[2]))
