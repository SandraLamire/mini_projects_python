# Global scope
name = "Sandra"
count = 1

# greeting(name) not necessary because of global scope, just greeting()
def greeting():
    # Local scope
    color = "blue"
    print(color)
    print(name)
    
greeting()
# print(color) = color is unknown here    

print("****************************")

def greeting2(firstname):
    # Local scope
    print(firstname)
    # Dave
    print(name)
    # Sandra
    
greeting2("Dave")

print("****************************")

def greeting3(name):
    # function parameter, not global scope name
    print(name)
    # John
    
greeting3("John")

print("****************************")

# Function scope
def another():
    color = "blue"
    # count += 1 : UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    # use keyword global to access to global count :
    global count
    count += 1
    # local count
    # count = 2
    print(count)
    
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("Dave")
    
another()
# 2
# red
# Dave

