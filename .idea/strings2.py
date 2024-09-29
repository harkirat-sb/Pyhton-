#        012345678901234
parrot= "Norwegian Blue"

print(parrot)

print(parrot[3])
# in line 6,3 is reffered as index....

print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])


#   Negative indexing is also present agar ham couting start kare end se
# 14-13-12-11-10-9-8-7-6-5-4-3-2-1
parrot= "Norwegian Blue"
print(parrot[-1])
print(parrot[-13])



#Slicing is a technique that is used to get a particular kind of words from letter
print(parrot[0:6])
#ab jaise jo word hai norweign usme se jab ham zero se counting karenge to 0-5 tak jo letters hoge wo  alag hojayenge and baak aur kuch nhai aaygea outpput
#agar 0-6 tak slicing hai to 0-5 count tak jitne letters honge they will slice

print(parrot[3:5]) #sirf 3 and 4 word aayega

print(parrot[10:14])

print(parrot[:6]+parrot[6:])





print(parrot[:])
print(parrot[-14:-8])


#slicing in steps
print(parrot[0:6:2])
#0-6 tak jitne words slicing mein ayenge unhe ham steps of 2 meun lenge jaise letter numbered 0,2and4 yeh slicing till 6 in steps of  2

print(parrot[0:6:3])
#slicing from 0-6 in steps of 3


numerical="12:1212121.12730,:1204437;21235'7;5'6383"

print(numerical[1::3])
