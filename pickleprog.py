import pickle
l=[10,20,30,40]
a=open('data1.txt','wb')
pickle.dump(l,a)
a.close()

f=open( a, 'rb')
pickle.load(f)
# f.close()