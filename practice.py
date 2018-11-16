from builtins import print, property

num=[90,55,10,20,30,40]
print(min(num))

print(max(num))
print(sum(num))
print(len(num))
print(num[-1])
print(num[-6])
num=['saurabh','singh',12.5,56,'S']
print(num)
num2=['i am','second','bro',12,93,0.8]
mill=[num,num2]
print(mill)

print(num.append(45))
print(num)
num.insert(1,'i am at 1 index')
print(num)

num.remove('S')
print(num)

num.pop(len(num)-2)
print(num)

print(num2)
num2.clear()
print(num2)
num2=['i am','second','bro',12,93,0.8]
print(num2)
del num2[3:]
print(num2)

num2.extend([12,93,0.8,17,18,19,20,21,22,23])
print(num2)

#sum(num2)
#print(num2)
del num2[0:3]
print(num2)
print(sum(num2))

num2.sort()
print(num2)

tuple={50,40,30,20,10}
print(tuple)
#commit2