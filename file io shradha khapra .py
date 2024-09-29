# to open a file - open("file_name","mode")
#mode can be r or w
# r: read mode
# w: write mode

f = open("blocks.py","r")
data = f.read()
# print(data)
# print(type(data))
# f.close()
# f = open("blocks.py","rt")
#
# #in case you want to print only first five letters
# date = f.read(5)
print(data)

line1 = f.readline()
print(line1)
