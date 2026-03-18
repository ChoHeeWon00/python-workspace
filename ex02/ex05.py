'''
file = open("C:\\ibm3-workspace/python-workspace/test2.txt", "a")
file.write("ssssss")
file.close()
'''
'''
file = open("C:\\ibm3-workspace/python-workspace/test2.txt", "r")
str_ = file.read()
file.close()
print( str_ )
'''
file = open("C:\\ibm3-workspace/python-workspace/test.jpg", "rb")
image = file.read()
file.close()

file = open("C:\\ibm3-workspace/python-workspace/복사이미지.jpg", "wb")
file.write(image)
file.close()