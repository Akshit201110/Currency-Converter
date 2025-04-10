import os 
words=''
all_c=[]
with open('currencies.txt') as c:
    for lines in c:
        words=lines.split('\t')
        for i in words:
            all_c.append(i.replace('\n',''))

count=1
df=1
for i in all_c:
    if count%2!=0:
        print(df,'.',i)
        df+=1
    count+=1


count=0
try:
    cn=int(input('Choose One Currensy Name And Write Its Number - '))
    cn+=cn
    cn-=1
except:
    print('\n')
    cn=int(input('Choose One Currensy Name And Only Write Numbers Instead Of Currency Name - '))
    cn+=cn
    cn-=1
    print('\n')

cr=int(input('Enter Currency - '))

w=0
for i in all_c:
    i=str(i)
    i=i.replace(' ','')
    i=i.lower()
    g=str(all_c[cn-1])
    g=g.replace(' ','')
    g=g.lower()
    if i == g:
        z=int(all_c[cn])
        print('Your Currency In Indian Rupees is :',cr*z)
        break
    w+=1
# print('Your Currency In Indian Rupees is :',cr*z)
# for i in all_c:
#     if count%2!=0:
#         if i == all_c[]:
#             pass
#     count+=1
