text = 'aa a aaa aaaa'
text2 = 'Aa a aaaa aaaaaaa'
text3='a aaaa'
mydict = dict()
for txt in [text,text2,text3]:
    for i in txt.split(' '):
        i=i.lower()
        mydict[i]=mydict.get(i,0)+1

print(mydict)