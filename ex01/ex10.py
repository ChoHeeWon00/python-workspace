import random
# range(1,5) => (1,5,1)
for i in range(5): #(0,5,1)
    print( random.random(), end=" ," )
print()
for i in range(5): #(0,5,1)
    print( random.randrange(1,3), end=" ," )