# Recursive function
def add_one(num):
    
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)

# add_one(0)
# # print 1 2 3 4 5 6 7 8 9 in vertical

mynewtotal = add_one(0)
print(mynewtotal)
# print 1 2 3 4 5 6 7 8 9 10 in vertical