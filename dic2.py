test_dic=  {'cod':2,'is': 2, 'best':2,'for': 2,'codin': 1}
print('T.O.d:'+ str(test_dic))
k=2
r=0
for key in test_dic:
    if test_dic[key]==k:
        r=r+1

print("FRequency of K is : "+str(r))