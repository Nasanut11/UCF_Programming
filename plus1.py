#%%

#This is an example ofhow to make a function
def addone(y):
    return y+1

#%%

x= 5
addone(x)
#%%
x= addone(x)
print(x)

#%%

for x in [2,3,4]:
    print(x**x)