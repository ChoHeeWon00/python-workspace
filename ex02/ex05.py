'''
file = open("C:\\ibm3-workspace/python-workspace/test2.txt", "a")
file.write("ssssss")
file.close()
'''
file = open("C:\\ibm3-workspace/python-workspace/test2.txt", "r")
str_ = file.read()
file.close()
print( str_ )