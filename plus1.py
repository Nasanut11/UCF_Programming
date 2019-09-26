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

#%%

def double(input,exponent):
    for x in input:
        print(x*2)
        
#%%

def exponent(x,y):
    z=x
    for n in range(1,y):
        z=z*x
    return z