# initialize game

def multiply(x,y):
    return(x**y)



def asleep(n):
    gueses = 6
    while gueses !=0:
        x = multiply(2,3)
        gueses -= n
    print(x)
    
asleep(2)