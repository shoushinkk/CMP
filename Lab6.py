import math
from scipy import optimize

x0 = 0.6
y0 = 0 

def f1(x):
    return(math.sin(x+1)-1)
def f2(y):
    return(1-(0.5*math.cos(y)))

def itr(e,x,y):
    xn = x 
    yn = y
    xn1 = f2(x) 
    yn1 = f1(xn1) 
    n = 1
    while((abs(xn1-xn)>=e)&(abs(yn1-yn)>=e)):
        xn = xn1 
        yn = yn1 
        xn1 = f2(xn) 
        yn1 = f1(yn) 
        n = n+1
    print('Method of simple iretations')
    print("X =x",xn1,'\nY =',yn1,'\nNumber if iterations',n)
    
itr(x0,y0,0.001)

def f(x):
    return math.sin(x[0]+1)-x[1]-1, 2*x[0]+math.cos(x[1])-2
    
sol = optimize.root(f,[0,0], method = 'Hybr')
print()
print('Check')
print (sol.x)
   