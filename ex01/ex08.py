ls = [10,20,30]
print( ls )
print( ls[1] )
print( len( ls ) )
print( ls[:] ) # 0 - 2
print( ls[1:3] ) # 1 - 2
print( ls[1:] ) # 1 - 끝까지

print("="*20)
import copy
#arr = ls
#arr = ls[:]
arr = copy.deepcopy( ls )
arr[0] = 12345
print(arr, id(arr) )
print(ls, id(ls) )

print("="*20)
print( ls*3 )
print( ls + arr )

print("="*20)
ls = [10,20,30]
ls.append(40)
print(ls)

ls.remove(20)
print(ls)

del( ls[1] )
print(ls)

ls.insert(1,12345)
print(ls)

print("="*20)
list = [10 , [100, 200, [1,2,3,4] ] , 30]

print( list[0] )
print( list[1] )
print( list[1][1] )
print( list[1][2][2] )

list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

list = [
    {"id":"aaa","n":"홍길동"},
    {"id":"bbb","n":"홍길동"},
    {"id":"ccc","n":"홍길동"},
]
print( list )